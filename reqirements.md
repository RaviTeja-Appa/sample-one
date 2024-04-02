# Pinterest - Software Requirements

## Step 1: Determine Your User

### User Persona: Ravi (Existing Pinterest User)

- **Name:** Ravi
- **Location:** Bangalore, India
- **Background:** Ravi is a 22-year-old software engineer living in Bangalore. He's been an active user of Pinterest for the past two years, using it to find inspiration for his photography projects, discover new travel destinations, and connect with like-minded individuals. Ravi is familiar with the platform's features and often shares his own content, including travel photos and tech tips.
- **Goals:**
  1. Continue finding inspiration for his photography projects and travel experiences.
  2. Explore new features and updates on Pinterest to enhance his user experience.
  3. Connect with other users, particularly those in the photography and tech communities, for networking and collaboration opportunities.
  4. Share his own content, including travel photos, tech articles, and personal projects, to inspire and engage with his followers.
- **Challenges:**
  1. Keeping up with the ever-growing content on Pinterest and finding ways to discover the most relevant and high-quality inspiration.
  2. Managing his boards and pins effectively to ensure they reflect his evolving interests and preferences.
  3. Balancing his time between consuming content and contributing to the Pinterest community through likes, comments, and shares.
  4. Adapting to changes in the platform's algorithms and user interface to optimize his user experience and content visibility.

### User Stories: Ravi (Existing User)

1. **Explore and Discover:**

   - As Ravi, I want to explore trending topics and categories on Pinterest to find inspiration for my photography projects and travel experiences.
   - As Ravi, I want to receive personalized recommendations based on my previous saves and activity on Pinterest.
   - As Ravi, I want to follow new users and boards aligned with my interests, such as photography, travel, and technology.

2. **Engage and Share:**

   - As Ravi, I want to like, comment on, and share Pins that resonate with me and inspire my creative pursuits.
   - As Ravi, I want to contribute my own content, including travel photos, tech articles, and personal projects, to share with my followers and the Pinterest community.
   - As Ravi, I want to engage with other users by participating in discussions, sharing insights, and offering feedback on their Pins.

3. **Manage and Customize:**
   - As Ravi, I want to organize my boards and pins effectively to reflect my evolving interests and preferences.
   - As Ravi, I want to customize my profile settings and preferences to optimize my user experience on Pinterest.
   - As Ravi, I want to explore new features and updates on Pinterest and provide feedback to the platform to help improve its usability and functionality.

### User Persona: Priya (New Pinterest User)

- **Name:** Priya
- **Location:** Bangalore, India
- **Background:** Priya is a 28-year-old fashion enthusiast and blogger from Bangalore. She has heard about Pinterest from her friends and colleagues who use it to discover fashion trends, outfit ideas, and styling tips. Excited to join the platform, Priya hopes to find inspiration for her blog posts, connect with fellow fashion bloggers, and explore new avenues to express her creativity.
- **Goals:**
  1. Discover the latest fashion trends and styling inspiration.
  2. Create boards to organize and save outfit ideas, fashion articles, and beauty tips.
  3. Follow fashion influencers, brands, and designers to stay updated on industry news and events.
  4. Engage with the Pinterest community through likes, comments, and shares on fashion-related content.
- **Challenges:**
  1. Navigating through the vast array of fashion content to find relevant and high-quality inspiration.
  2. Understanding how to effectively use boards and pins to curate her fashion collections.
  3. Building her presence on the platform and establishing connections with other fashion enthusiasts and bloggers.
  4. Overcoming any technical hurdles or unfamiliarity with Pinterest's interface and features.

### User Stories: Priya (New User)

1. **Explore and Discover:**

   - As Priya, I want to browse through fashion categories and explore trending styles and outfit ideas on Pinterest.
   - As Priya, I want to search for specific fashion trends, brands, and influencers to discover new sources of inspiration.
   - As Priya, I want to receive personalized recommendations based on my fashion preferences and browsing history.

2. **Create and Organize:**

   - As Priya, I want to create boards to organize my favorite outfit ideas, fashion articles, and beauty tips on Pinterest.
   - As Priya, I want to save Pins to my boards and add descriptions and tags to categorize and organize my fashion collections.
   - As Priya, I want to curate my profile and showcase my personal style and fashion preferences to the Pinterest community.

3. **Connect and Engage:**
   - As Priya, I want to follow fashion influencers, brands, and designers to stay updated on the latest industry news, trends, and events.
   - As Priya, I want to engage with other Pinterest users by liking, commenting on, and sharing fashion-related Pins.
   - As Priya, I want to join fashion communities and group boards to connect with like-minded individuals and share ideas and inspiration.

## Database Schema

### Users Table:

- **user_id**: Primary key
- **username**: Unique
- **email**: Unique
- **password**: Encrypted
- **profile_picture**: URL to profile picture
- **bio**: User's biography

### Boards Table:

- **board_id**: Primary key
- **user_id**: Foreign key to Users table
- **name**: Name of the board
- **description**: Description of the board
- **created_at**: Timestamp

### Pins Table:

- **pin_id**: Primary key
- **user_id**: Foreign key to Users table
- **board_id**: Foreign key to Boards table
- **title**: Title of the pin
- **description**: Description of the pin
- **image_url**: URL to the pin image or video
- **created_at**: Timestamp

### Likes Table:

- **like_id**: Primary key
- **user_id**: Foreign key to Users table
- **pin_id**: Foreign key to Pins table
- **created_at**: Timestamp

### Comments Table:

- **comment_id**: Primary key
- **user_id**: Foreign key to Users table
- **pin_id**: Foreign key to Pins table
- **comment_text**: Text of the comment
- **created_at**: Timestamp

### Follows Table (for user follows):

- **follow_id**: Primary key
- **follower_id**: Foreign key to Users table
- **followed_id**: Foreign key to Users table
- **created_at**: Timestamp

## Database Management System (DBMS)

You can choose a suitable database management system (DBMS) for your project. Common choices include:

- **Relational Database Management System (RDBMS)**: Such as MySQL, PostgreSQL, or SQLite, which are suitable for structured data with relationships between tables.
- Currently In this project we are using PostgreSQL

## ORM (Object-Relational Mapping)

Consider using an ORM library like SQLAlchemy (for Python) or Sequelize (for Node.js) to interact with your database from your application code. This can simplify database operations and help manage your database schema more effectively.
