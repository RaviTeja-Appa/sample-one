from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from authentications.models import User
from .forms import PinCreationForm, PinUpdateForm
from .models import Image_Posting, Board, Comment, Like, Following
from .forms import BoardForm


from django.http import JsonResponse
from .models import Image_Posting


def home(request):
    images = Image_Posting.objects.all()
    data = {
        'images': [{
            'pk': image.pk,
            'url': image.image_Post.url
        } for image in images]
    }
    return JsonResponse(data)


@login_required
def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            # Redirect back to the previous page or to a default URL if no referer is available
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = BoardForm()
    return render(request, 'create_board.html', {'form': form, 'user': request.user})


@login_required
def board_list(request):
    print('\n printing the user details:\n', request.user)
    boards = Board.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'board_list.html', {'boards': boards, 'user': request.user})


# the image uploading or pin uploadiung

@login_required
def create_pin(request):
    if request.method == 'POST':
        form = PinCreationForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            pin = form.save(commit=False)  # Don't commit right away
            pin.user = request.user  # Assign current user
            pin.save()
            # Save the pin object after setting the user
            image_obj = get_object_or_404(
                Image_Posting, user=pin.user.id, image_Post=pin.image_Post)
            print('\n\n', pin.image_Post, image_obj.id, '\n\n',)
            context = {
                'image_id': image_obj.id,
                'form': PinCreationForm(user=request.user),
                'alert': 'Do you want to see your post'
            }
            # Redirect to list view
            return render(request, 'create_pin.html', context)
    else:
        # Pass user to form during form initialization in the template
        # No user argument here
        context = {'form': PinCreationForm(user=request.user)}
        return render(request, 'create_pin.html', context)


@login_required
def list_pins(request):
    # Filter by currently logged-in user
    pins = Image_Posting.objects.filter(user=request.user.id)
    return render(request, 'list_pins.html', {'pins': pins, 'user': request.user})


@login_required
def update_pin(request, pin_id):
    pin = Image_Posting.objects.get(pk=pin_id)

    if request.method == 'POST':
        form = PinUpdateForm(request.POST, request.FILES, instance=pin)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PinUpdateForm(instance=pin)

    context = {'form': form, 'pin': pin}
    return render(request, 'update_pin.html', context)


@login_required
def delete_pin(request, pin_id):
    pin = Image_Posting.objects.get(pk=pin_id)
    pin.delete()
    return redirect('list_pins')
# Updating Pins
# @login_required
# def update_pin(request,)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Image_Posting, pk=pk)
    likes_count = Like.objects.filter(image_post=post).count()
    liked = Like.objects.filter(
        image_post=post, liked_by=request.user).exists()
    comments = Comment.objects.filter(image_post=post)
    comments_count = comments.count()
    user = get_object_or_404(User, id=post.user.id)
    followers_count = Following.objects.filter(user=user).count()
    is_following = Following.objects.filter(
        user=user, followed_by=request.user).exists()
    reuested_user = request.user
    # print(f'\n\n {request.user.user_image.url} \n\n')
    if is_following:
        following_relation = Following.objects.get(
            user=user, followed_by=request.user)
        following_id = following_relation.id
        print(f'\n\n {following_id} \n\n')
    else:
        following_id = None
        print(f'\n\n {following_id} \n\n')

    context = {
        'post': post,
        'liked': liked,
        'likes_count': likes_count,
        'comments': comments,
        'followers_count': followers_count,
        'user': user,
        'comments_count': comments_count,
        'is_following': is_following,
        'following_id': following_id,
        'reuested_user': reuested_user  # Pass the flag to the template
    }
    return render(request, 'modification.html', context)


@login_required
def like_post(request, pk):
    post = get_object_or_404(Image_Posting, pk=pk)
    liked = Like.objects.filter(
        image_post=post, liked_by=request.user).exists()

    if liked:
        like = Like.objects.get(image_post=post, liked_by=request.user)
        like.like_count -= 1
        like.save()
        like.delete()
    else:
        like = Like(image_post=post, liked_by=request.user, user=post.user)
        like.like_count += 1
        like.save()

    post.save()
    return redirect('post_detail', pk=pk)


# creating and displaying the comments


@login_required
def add_comment(request, image_post_id):
    image_post = get_object_or_404(Image_Posting, pk=image_post_id)
    existing_comment = Comment.objects.filter(
        image_post=image_post, user=request.user).exists()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print(f'\n\n going through unfollow \n\n')
            comment = form.save(commit=False)
            comment.user = image_post.user
            comment.image_post = image_post
            comment.commented_by = request.user
            comment.save()
            return redirect('post_detail', pk=image_post_id)
    else:
        form = CommentForm()

    # return render(request, 'add_comment.html', {'form': form})


@login_required
def list_comments(request, image_post_id):
    image_post = get_object_or_404(Image_Posting, pk=image_post_id)
    comments = Comment.objects.filter(image_post=image_post)
    return render(request, 'list_comments.html', {'image_post': image_post, 'comments': comments})


@login_required
def adding_followers(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if user_to_follow == request.user:
        return redirect('profile')

    Following.objects.get_or_create(
        user=user_to_follow, followed_by=request.user)

    referring_url = request.META.get('HTTP_REFERER')
    if referring_url and 'post/' in referring_url:
        url_parts = referring_url.split('/')
        image_id_index = url_parts.index('post') + 1

        image_post_id = url_parts[image_id_index]

        return redirect('post_detail', pk=image_post_id)

    return redirect('profile', pk=user_to_follow.id)


@login_required
def removing_follower(request, follower_id):
    follower = get_object_or_404(User, id=follower_id)

    if follower == request.user:
        return redirect('profile')

    follower_relation = Following.objects.filter(
        user=request.user, followed_by=follower).first()

    if follower_relation:
        follower_relation.delete()

    return redirect('profile', pk=request.user.id)


@login_required
def unfollowing(request, following_id):

    following_relation = get_object_or_404(
        Following, id=following_id, followed_by=request.user)
    following_relation.delete()
    referring_url = request.META.get('HTTP_REFERER')
    if referring_url and 'post/' in referring_url:
        url_parts = referring_url.split('/')
        image_id_index = url_parts.index('post') + 1

        image_post_id = url_parts[image_id_index]
        return redirect('post_detail', pk=image_post_id)
    return redirect('profile', pk=following_relation.user.id)


@login_required
def profile(request, pk=None):  # Add user_id parameter with a default value
    if pk:
        user = get_object_or_404(User, id=pk)
    else:
        user = request.user
    requested_user = request.user
    followers_count = Following.objects.filter(user=user).count()
    following_count = Following.objects.filter(followed_by=user).count()
    followers_list = Following.objects.filter(user=user)
    following_list = Following.objects.filter(followed_by=user)
    is_following = Following.objects.filter(
        user=user, followed_by=request.user).exists()
    user_posts = Image_Posting.objects.filter(user=user.id)

    if is_following:
        following_relation = Following.objects.get(
            user=user, followed_by=request.user)
        following_id = following_relation.id
        print('\n\n {following_id} \n\n')
    else:
        following_id = None

    context = {
        'user_posts': user_posts,
        'requested_user': requested_user,
        'user': user,
        'followers_count': followers_count,
        'following_count': following_count,
        'followers_list': followers_list,
        'following_list': following_list,
        'is_following': is_following,
        'following_id': following_id,  # Pass following_id to template
    }
    return render(request, 'profile.html', context)


@login_required
def saving_Post(request, pk=None):

    if pk:
        image_data = get_object_or_404(Image_Posting, id=pk)
