# Django Social Media Backend
## Introduction
This project is a complete backend of any social media project. It contains all the necessary functionality that a social media needs.
If you need additional functionality, feel free to add them accordingly!

## Features
This project contains the following features along with an admin panel and API's.
- Authentication: Ability to register, login, change password, reset password, verify email address and logout. It contains the following API's.
    - Login API
    - Logout API
    - Register API
    - Change Password API
    - Reset Password API
    - Reset Password Confirmation API
    - Email Verify API
    - Email Verification Confirmation API
- Profile Management: Ability to view profile, update language, country, religion and profile picture. It contains the following API's.
    - Get Profile API
    - Update Country API
    - Update Language API
    - Update Religion API
    - Update Profile Picture API
- Feedback: The users will be able to write feedback and give rating about the experience of the application and suggest desired improvements and report bug. It ha one API.
    - Post Feedback API
    - Report a Bug API
- Configuration: The admin will be able to set the available countries, religions and languages via the admin panel. It has 3 API's for the application.
    - Get All Countries API
    - Get All Languages API
    - Get All Religions API
- Friend: Ability to perform all friend related functionality.
    - Send Friend Request API
    - Get All Friends API
    - Get All Sent Request API
    - Get All Received Request API
    - Accept Friend Request API
    - Cancel Friend Request API
    - Reject Friend Request API
    - Friend Suggestions API
    - Search Friend API
    - Un-Friend API
    - Block User API
    - Un-Block User API
    - Get All Blocked User API
- Feed: Ability to post, like, comment and view other's post.
    - Create Post API
    - Update Post API
    - Delete Post API
    - Get All My Posts API
    - Get Post Details API
    - Get My Feed API
    - Like Post API
    - Add Comment API
    - Edit Comment API
    - Delete Comment API
    - Like Comment API

## Database design
### Account
#### User
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| ID                                      | Integer                       |
| Password                                | String                        |
| Email                                   | Email                         |
| First name                              | String                        |
| Last name                               | String                        |
| Country                                 | String                        |
| Language                                | String                        |
| Religion                                | String                        |
| Avatar                                  | Image Field                   |
| Date Joined                             | Date Time                     |
| Last Login                              | Date Time                     |
| Is Active                               | Boolean                       |
| Is Staff                                | Boolean                       |

#### Token Manager
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| Key                                     | String                        |
| Email                                   | Email                         |
| Date Created                            | Date Time                     |

### Configuration
#### Country
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| ID                                      | Integer                       |
| Country                                 | String                        |

#### Language
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| ID                                      | Integer                       |
| Language                                | String                        |

#### Religion
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| ID                                      | Integer                       |
| Religion                                | String                        |

### Feedback
#### FeedBack
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| ID                                      | Integer                       |
| Feedback Provider                       | Foreign Key to User Model     |
| Feedback                                | Text Field                    |
| Rating                                  | Decimal Fields                |
| Date Posted                             | Date Time                     |

#### BugReport
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| ID                                      | Integer                       |
| Bug Reporter                            | Foreign Key to User Model     |
| Bug Information                         | Text Field                    |
| Date Posted                             | Date Time                     |

### Friend
#### FriendRequest
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| ID                                      | Integer                       |
| Sender                                  | Foreign Key to User Model     |
| Receiver                                | Foreign Key to User Model     |
| request Send Date                       | Date Time                     |

#### FriendshipMapper
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| ID                                      | Integer                       |
| User 1                                  | Foreign Key to User Model     |
| User 2                                  | Foreign Key to User Model     |
| request Accept Date                     | Date Time                     |

#### BlockedUser
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| ID                                      | Integer                       |
| Blocker                                 | Foreign Key to User Model     |
| Blocked                                 | Foreign Key to User Model     |
| Block Date                              | Date Time                     |

### Feed
#### Post
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| Post                                    | TextField                     |
| date Created                            | Date Time                     |
| Is Edited                               | Boolean                       |
| Date Edited                             | Date Time                     |
| Author                                  | Foreign Key to User Model     |
| Attachment                              | File Field                    |
| Post Privacy                            | String                        |
| Likes                                   | Foreign Key to User Model     |

#### Comment
| Attribute                               | Data Type                     |
|:----------------------------------------|:------------------------------|
| Post                                    | Foreign Key to Post Model     |
| Comment                                 | TextField                     |
| date Created                            | Date Time                     |
| Is Edited                               | Boolean                       |
| Date Edited                             | Date Time                     |
| Author                                  | Foreign Key to User Model     |
| Attachment                              | File Field                    |
| Likes                                   | Foreign Key to User Model     |

## Api Documentation
### Account
#### Verify Email Api
- URL endpoint: api/account/auth/verify-email/
- Authentication required: False
- Request method: POST
- Request:
    ```json
    {
        "email": "hello@gmail.com"
    }
    ```
- Response:
    ```json
    {
        "success": "An email with a verification code is sent to the email."
    }
    ```
    or
    ```json
    {
        "error": "This email is already taken.",
        "details": [
            "email: Email already taken. Please provide a unique email."
        ]
    }
    ```
    or
    ```json
    {
        "error": "Invalid request format.",
        "details": [
            "email: This field is required."
        ]
    }
    ```
#### Confirm Email Verification Api
- URL endpoint: api/account/auth/confirm-email-verification/
- Authentication required: False
- Request method: POST
- Request:
    ```json
    {
        "email": "hello@gmail.com",
        "verification_code": "XMPQUE"
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! Email is verified."
    }
    ```
    or
    ```json
    {
        "error": "Security code invalid or expired./Email and token mismatch.",
        "details": [
            "The code you provided is invalid. Please provide a valid code."
        ]
    }
    ```
    or
    ```json
    {
        "error": "Invalid request format.",
        "details": [
            "email: This field is required."
        ]
    }
    ```
#### Register Api
- URL endpoint: api/account/auth/register/
- Authentication required: False
- Request method: POST
- Request:
    ```json
    {
        "email": "hello@gmail.com",
        "first_name": "Hello",
        "last_name": "Gello",
        "password": "HelloGello"
    }
    ```
- Response:
    ```json
    {
        "id": 4,
        "email": "hello@gmail.com",
        "first_name": "Hello",
        "last_name": "Gello",
        "auth_token": "e7f08c4767cd9bec14f53239ee18665db82e80e8",
        "date_joined": "2021-01-22T17:35:06.867862Z",
        "country": "",
        "language": "",
        "religion": "",
        "avatar": null
    }
    ```
    or
    ```json
    {
        "error": "Invalid email or password.",
        "details": [
            "The email and password do not match. Please try with a valid combination."
        ]
    }
    ```
    or
    ```json
    {
        "error": "Invalid request format.",
        "details": [
            "email: This field is required.",
            "password: This field is required."
        ]
    }
    ```
#### Login Api
- URL endpoint: api/account/auth/login/
- Authentication required: False
- Request method: POST
- Request:
    ```json
    {
        "email": "myemail@gmail.com",
        "password": "mypassword"
    }
    ```
- Response:
    ```json
    {
        "id": 2,
        "email": "hello@hello.com",
        "first_name": "Hello",
        "last_name": "Gello",
        "auth_token": "823397948b3770b8fe7c5b5bc5225fe9d7a4bfba",
        "date_joined": "2021-01-22T16:59:08.649053Z",
        "country": "Bangladesh",
        "language": "English",
        "religion": "Islam",
        "avatar": "/media/profile_pictures/404_Error_Page_not_Found_with_people_connecting_a_plug-bro.png"
    }
    ```
    or
    ```json
    {
        "error": "Invalid email or password.",
        "details": [
            "The email and password do not match. Please try with a valid combination."
        ]
    }
    ```
    or
    ```json
    {
        "error": "Invalid request format.",
        "details": [
            "email: This field is required.",
            "password: This field is required."
        ]
    }
    ```
#### Logout Api
- URL endpoint: api/account/auth/logout/
- Authentication required: True (add "Authorization: Token your-token-here" to the request header)
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! You have been logged out."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided./Invalid token."
    }
    ```
#### Change Password Api
- URL endpoint: api/account/auth/change-password/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "current_password": "hello",
        "new_password": "buddy",
        "new_password_2": "buddy"
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! Password change successful!/Authentication credentials were not provided."
    }
    ```
    or
    ```json
    {
        "error": "New passwords do not match.",
        "details": [
            "Please provide same password for both new password fields."
        ]
    }
    ```
#### Reset Password Api
- URL endpoint: api/account/auth/reset-password/
- Authentication required: False
- Request method: POST
- Request: 
    ```json
    {
        "email": "hello@example.com"
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! You will receive an email shortly if you are registered. Check your inbox for password reset token."
    }
    ```
    or
    ```json
    {
        "error": "Invalid request format.",
        "details": [
            "email: This field is required."
        ]
    }
    ```
#### Confirm Password Reset Api
- URL endpoint: api/account/auth/confirm-password-reset/
- Authentication required: False
- Request method: POST
- Request: 
    ```json
    {
        "email": "hello@gmail.com",
        "token": "ABCDEF",
        "new_password": "abcdef",
        "new_password_2": "abcdef"
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! Password reset successful. Please login with your new password."
    }
    ```
    or
    ```json
    {
        "error": "Security code invalid or expired.",
        "details": [
            "The code you provided is invalid. Please provide a valid code."
        ]
    }
    ```
  
### Profile
#### Get Profile API
- URL endpoint: api/account/profile/get-profile/
- Authentication required: True
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "id": 2,
        "email": "hello@hello.com",
        "first_name": "Hello",
        "last_name": "Gello",
        "auth_token": "43a6e82e4304cef1f83e1b939b522293233d59a6",
        "date_joined": "2021-01-22T16:59:08.649053Z",
        "country": "Bangladesh",
        "language": "English",
        "religion": "Islam",
        "avatar": "/media/profile_pictures/404_Error_Page_not_Found_with_people_connecting_a_plug-bro.png"
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided./Invalid token."
    }
    ```
#### Update Country API
- URL endpoint: api/account/profile/update-country/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "value": "United States"
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! Country has been updated./Error! Something went wrong. Please try again later."
    }
    ```
#### Update Language API
- URL endpoint: api/account/profile/update-language/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "value": "Chinese"
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! Language has been updated./Error! Something went wrong. Please try again later."
    }
    ```
#### Update Religion API
- URL endpoint: api/account/profile/update-religion/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "value": "Christian"
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! Religion has been updated./Error! Something went wrong. Please try again later."
    }
    ```
#### Update Profile Picture API
- URL endpoint: api/api/account/profile/update-avatar/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "avatar": "<File as multipart form data>"
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! Profile picture has been updated.",
        "avatar": "/media/profile_pictures/3.jpg"
    }
    ```
    or
    ```json
    {
        "detail": "Error! Something went wrong. Please try again later.",
        "avatar": ""
    }
    ```


### Configuration
#### Get All Countries Api
- URL endpoint: api/configuration/all-countries/
- Authentication required: False
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "countries": []
    }
    ```
    or
    ```json
    {
        "countries": [
            {
                "id": 2,
                "country": "Bangladesh"
            },
            {
                "id": 3,
                "country": "Canada"
            },
            {
                "id": 1,
                "country": "USA"
            }
        ]
    }
    ```
#### Get All Languages Api
- URL endpoint: api/configuration/all-languages/
- Authentication required: False
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "languages": []
    }
    ```
    or
    ```json
    {
        "languages": [
            {
                "id": 2,
                "language": "Bengali"
            },
            {
                "id": 1,
                "language": "English"
            }
        ]
    }
    ```
#### Get All Religions Api
- URL endpoint: api/configuration/all-religions/
- Authentication required: False
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "religions": []
    }
    ```
    or
    ```json
    {
        "religions": [
            {
                "id": 2,
                "religion": "Christian"
            },
            {
                "id": 1,
                "religion": "Islam"
            }
        ]
    }
    ```

### Feedback
#### Post Feedback Api
- URL endpoint: api/feedback/post-feedback/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "feedback": "Your app is awsome. Keep it up!",
        "rating": 5
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! Thanks for your feedback. Your feedback has been sent to the authority."
    }
    ```
    ```json
    {
        "detail": "Error! Something went wrong. Please try again later."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Report Bug Api
- URL endpoint: api/feedback/report-bug/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "bug_information": "Please fix the bug in chat!"
    }
    ```
- Response:
    ```json
    {
        "detail": "Success! Thanks for reporting the issue. Your concern has been sent to the authority."
    }
    ```
    ```json
    {
        "detail": "Error! Something went wrong. Please try again later."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```

### Friend
#### Send Friend Request API
- URL endpoint: api/friends/send-friend-request/<user_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! Friend request sent."
    }
    ```
    ```json
    {
        "detail": "Error! Receiver does not exists./Error! You can not send friend request to yourself./You have already sent a friend request to this person."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Get All Friends API
- URL endpoint: api/friends/get-all-friends/
- Authentication required: True
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "all_friends": [
            {
                "friend": {
                    "id": 2,
                    "email": "kaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "United States",
                    "language": "Chinese",
                    "religion": "Islam-Sunni",
                    "avatar": "/media/profile_pictures/reza.jpg"
                },
                "friend_since": "2021-02-15T13:51:37.757921Z"
            },
            {
                "friend": {
                    "id": 3,
                    "email": "abcdkaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "friend_since": "2021-02-15T13:51:46.315257Z"
            },
            {
                "friend": {
                    "id": 2,
                    "email": "kaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "United States",
                    "language": "Chinese",
                    "religion": "Islam-Sunni",
                    "avatar": "/media/profile_pictures/reza.jpg"
                },
                "friend_since": "2021-02-15T14:00:22.836795Z"
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Get All Sent Request API
- URL endpoint: api/friends/get-all-sent-request/
- Authentication required: True
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "all_sent_requests": [
            {
                "id": 1,
                "receiver": {
                    "id": 2,
                    "email": "kaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "United States",
                    "language": "Chinese",
                    "religion": "Islam-Sunni",
                    "avatar": "/media/profile_pictures/reza.jpg"
                },
                "request_send_date": "2021-02-15T13:41:22.346349Z"
            },
            {
                "id": 2,
                "receiver": {
                    "id": 3,
                    "email": "abcdkaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "request_send_date": "2021-02-15T14:31:32.990444Z"
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Get All Received Request API
- URL endpoint: api/friends/get-all-received-request/
- Authentication required: True
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "all_received_requests": [
            {
                "id": 3,
                "sender": {
                    "id": 2,
                    "email": "kaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "United States",
                    "language": "Chinese",
                    "religion": "Islam-Sunni",
                    "avatar": "/media/profile_pictures/reza.jpg"
                },
                "request_send_date": "2021-02-15T14:42:04.875113Z"
            },
            {
                "id": 4,
                "sender": {
                    "id": 3,
                    "email": "abcdkaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "request_send_date": "2021-02-15T14:42:11.156738Z"
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Un-Friend API
- URL endpoint: api/friends/un-friend/<user_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! You have been un-friend."
    }
    ```
    or
    ```json
    {
        "detail": "Error! you are not friend with this person."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Accept Friend Request API
- URL endpoint: api/friends/accept-friend-request/<request_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! Friend request accepted."
    }
    ```
    or
    ```json
    {
        "detail": "Error! Friend request does not exist."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Reject Friend Request API
- URL endpoint: api/friends/reject-friend-request/<request_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! Friend request rejected."
    }
    ```
    or
    ```json
    {
        "detail": "Error! Friend request does not exist."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Cancel Friend Request API
- URL endpoint: api/friends/cancel-friend-request/<request_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! Friend request cancelled."
    }
    ```
    or
    ```json
    {
        "detail": "Error! Friend request does not exist."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Friend Suggestions API
- URL endpoint: api/friends/friend-suggestions/
- Authentication required: True
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "suggestions": [
            {
                "id": 6,
                "email": "mdnyrr22222eza@gmail.com",
                "first_name": "d",
                "last_name": "d",
                "country": "Australia",
                "language": "English",
                "religion": "islam",
                "avatar": null
            },
            {
                "id": 3,
                "email": "abcdkaykobadreza@gmail.com",
                "first_name": "Kaykobad",
                "last_name": "Reza",
                "country": "",
                "language": "",
                "religion": "",
                "avatar": null
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Search People API
- URL endpoint: api/friends/search-people/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "search_keyword": "kaykobad"
    }
    ```
- Response:
    ```json
    {
        "search_result": [
            {
                "user": {
                    "id": 2,
                    "email": "kaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "United States",
                    "language": "Chinese",
                    "religion": "Islam-Sunni",
                    "avatar": "/media/profile_pictures/reza.jpg"
                },
                "is_friend": true
            },
            {
                "user": {
                    "id": 3,
                    "email": "abcdkaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "is_friend": false
            },
            {
                "user": {
                    "id": 5,
                    "email": "kaykobad.reza@bkash.com",
                    "first_name": "f",
                    "last_name": "f",
                    "country": "Bangladesh",
                    "language": "English",
                    "religion": "Islam",
                    "avatar": null
                },
                "is_friend": false
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Error! Something went wrong. Please try again later."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Block User API
- URL endpoint: api/friends/block/<user_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! User is blocked."
    }
    ```
    or
    ```json
    {
        "detail": "Error! User does not exist./Error! You can not block yourself."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Un-Block User API
- URL endpoint: api/friends/unblock/<user_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! User is unblocked."
    }
    ```
    or
    ```json
    {
        "detail": "Error! Blocked user does not exist."
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
#### Get Blocked User API
- URL endpoint: api/friends/get-blocked-users/
- Authentication required: True
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "blocked_users": [
            {
                "id": 3,
                "email": "abcdkaykobadreza@gmail.com",
                "first_name": "Kaykobad",
                "last_name": "Reza",
                "country": "",
                "language": "",
                "religion": "",
                "avatar": null
            },
            {
                "id": 4,
                "email": "user1234@gmail.com",
                "first_name": "H",
                "last_name": "P",
                "country": "Bangladesh",
                "language": "English",
                "religion": "Islam",
                "avatar": null
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```

### Feed
#### Create Post API
- URL endpoint: api/feed/create-post/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "post": "This is my first post. Hope you like it!"
    }
    ```
- Response:
    ```json
    {
        "id": 1,
        "post": "This is my first post. Hope you like it!",
        "date_created": "2021-02-18T15:18:32.934753Z",
        "is_edited": false,
        "date_edited": null,
        "author": {
            "id": 1,
            "email": "admin@admin.com",
            "first_name": "",
            "last_name": "",
            "country": "",
            "language": "",
            "religion": "",
            "avatar": null
        },
        "total_likes": 0,
        "total_comments": 0,
        "attachment": null,
        "post_privacy": "friends"
    }
    ```
    or
    ```json
    {
        "detail": "Error! Something went wrong. Please try again later."
    }
    ```
#### Update Post API
- URL endpoint: api/feed/update-post/<post_id>/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "post": "This is my updated second post. Hope you like it too!"
    }
    ```
- Response:
    ```json
    {
        "id": 2,
        "post": "This is my updated second post. Hope you like it too!",
        "date_created": "2021-02-18T15:21:37.336042Z",
        "is_edited": true,
        "date_edited": "2021-02-19T04:33:57.477683Z",
        "author": {
            "id": 1,
            "email": "admin@admin.com",
            "first_name": "",
            "last_name": "",
            "country": "",
            "language": "",
            "religion": "",
            "avatar": null
        },
        "total_likes": 2,
        "total_comments": 2,
        "attachment": null,
        "post_privacy": "friends",
        "comments": [
            {
                "id": 1,
                "comment": "This is my first updated comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 2,
                "post_text": "This is my updated second post. Hope you like it too!",
                "date_created": "2021-02-19T04:06:04.054386Z",
                "is_edited": true,
                "date_edited": "2021-02-19T04:11:15.009832Z",
                "attachment": null,
                "total_likes": 1
            },
            {
                "id": 2,
                "comment": "This is my first comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 2,
                "post_text": "This is my updated second post. Hope you like it too!",
                "date_created": "2021-02-19T04:06:11.572011Z",
                "is_edited": false,
                "date_edited": null,
                "attachment": null,
                "total_likes": 1
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Error! No post found. Make sure you are the author of the post and try with a valid post id."
    }
    ```
#### My All Posts API
- URL endpoint: api/feed/my-posts/
- Authentication required: True
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "posts": [
            {
                "id": 1,
                "post": "This is my first post. Hope you like it!",
                "date_created": "2021-02-18T15:18:32.934753Z",
                "is_edited": false,
                "date_edited": null,
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "total_likes": 0,
                "total_comments": 0,
                "attachment": null,
                "post_privacy": "friends"
            },
            {
                "id": 2,
                "post": "This is my updated second post. Hope you like it too!",
                "date_created": "2021-02-18T15:21:37.336042Z",
                "is_edited": true,
                "date_edited": "2021-02-18T16:51:27.678950Z",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "total_likes": 0,
                "total_comments": 0,
                "attachment": null,
                "post_privacy": "friends"
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Error! No post found. Make sure you are the author of the post and try with a valid post id."
    }
    ```
#### Delete Post API
- URL endpoint: api/feed/delete-post/<post_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! Post deleted from database."
    }
    ```
    or
    ```json
    {
        "detail": "Error! Post does not exist."
    }
    ```
#### Post Details API
- URL endpoint: api/feed/post-details/<post_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "id": 2,
        "post": "This is my updated second post. Hope you like it too!",
        "date_created": "2021-02-18T15:21:37.336042Z",
        "is_edited": true,
        "date_edited": "2021-02-19T04:33:57.477683Z",
        "author": {
            "id": 1,
            "email": "admin@admin.com",
            "first_name": "",
            "last_name": "",
            "country": "",
            "language": "",
            "religion": "",
            "avatar": null
        },
        "total_likes": 2,
        "total_comments": 2,
        "attachment": null,
        "post_privacy": "friends",
        "comments": [
            {
                "id": 1,
                "comment": "This is my first updated comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 2,
                "post_text": "This is my updated second post. Hope you like it too!",
                "date_created": "2021-02-19T04:06:04.054386Z",
                "is_edited": true,
                "date_edited": "2021-02-19T04:11:15.009832Z",
                "attachment": null,
                "total_likes": 1
            },
            {
                "id": 2,
                "comment": "This is my first comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 2,
                "post_text": "This is my updated second post. Hope you like it too!",
                "date_created": "2021-02-19T04:06:11.572011Z",
                "is_edited": false,
                "date_edited": null,
                "attachment": null,
                "total_likes": 1
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Error! Post does not exist."
    }
    ```
#### Like Post API
- URL endpoint: api/feed/like-post/<post_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! You liked/unliked the post."
    }
    ```
    or
    ```json
    {
        "detail": "Error! Post does not exist./Error! You already liked the post."
    }
    ```
#### My Feed API (Will return only friends post)
- URL endpoint: api/feed/my-feed/
- Authentication required: True
- Request method: GET
- Request: None
- Response:
    ```json
    {
        "posts": [
            {
                "id": 3,
                "post": "This is a post for the app! Like it, if you like it.",
                "date_created": "2021-02-19T03:53:22.046432Z",
                "is_edited": false,
                "date_edited": "2021-02-19T03:53:05Z",
                "author": {
                    "id": 2,
                    "email": "kaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "United States",
                    "language": "Chinese",
                    "religion": "Islam-Sunni",
                    "avatar": "/media/profile_pictures/reza.jpg"
                },
                "total_likes": 0,
                "total_comments": 0,
                "attachment": null,
                "post_privacy": "friends"
            },
            {
                "id": 4,
                "post": "This is a post for the app! Like it, if you like it.",
                "date_created": "2021-02-19T03:53:37.831118Z",
                "is_edited": true,
                "date_edited": "2021-02-19T03:53:25Z",
                "author": {
                    "id": 3,
                    "email": "abcdkaykobadreza@gmail.com",
                    "first_name": "Kaykobad",
                    "last_name": "Reza",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "total_likes": 0,
                "total_comments": 0,
                "attachment": null,
                "post_privacy": "friends"
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Error! Something went wrong. Please try again later."
    }
    ```
#### Add Comment API
- URL endpoint: api/feed/add-comment/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "post_id": 1,
        "comment": "This is my first comment for testing."
    }
    ```
- Response:
    ```json
    {
        "id": 2,
        "post": "This is my updated second post. Hope you like it too!",
        "date_created": "2021-02-18T15:21:37.336042Z",
        "is_edited": true,
        "date_edited": "2021-02-18T17:24:25.163796Z",
        "author": {
            "id": 1,
            "email": "admin@admin.com",
            "first_name": "",
            "last_name": "",
            "country": "",
            "language": "",
            "religion": "",
            "avatar": null
        },
        "total_likes": 1,
        "total_comments": 2,
        "attachment": null,
        "post_privacy": "friends",
        "comments": [
            {
                "id": 1,
                "comment": "This is my first comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 2,
                "post_text": "This is my updated second post. Hope you like it too!",
                "date_created": "2021-02-19T04:06:04.054386Z",
                "is_edited": false,
                "date_edited": null,
                "attachment": null,
                "total_likes": 0
            },
            {
                "id": 2,
                "comment": "This is my first comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 2,
                "post_text": "This is my updated second post. Hope you like it too!",
                "date_created": "2021-02-19T04:06:11.572011Z",
                "is_edited": false,
                "date_edited": null,
                "attachment": null,
                "total_likes": 0
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Could not comment. Invalid post id or comment format."
    }
    ```
#### Update Comment API
- URL endpoint: api/feed/update-comment/<comment_id>/
- Authentication required: True
- Request method: POST
- Request: 
    ```json
    {
        "comment": "This is my first comment for testing."
    }
    ```
- Response:
    ```json
    {
        "id": 2,
        "post": "This is my updated second post. Hope you like it too!",
        "date_created": "2021-02-18T15:21:37.336042Z",
        "is_edited": true,
        "date_edited": "2021-02-18T17:24:25.163796Z",
        "author": {
            "id": 1,
            "email": "admin@admin.com",
            "first_name": "",
            "last_name": "",
            "country": "",
            "language": "",
            "religion": "",
            "avatar": null
        },
        "total_likes": 1,
        "total_comments": 2,
        "attachment": null,
        "post_privacy": "friends",
        "comments": [
            {
                "id": 1,
                "comment": "This is my first updated comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 2,
                "post_text": "This is my updated second post. Hope you like it too!",
                "date_created": "2021-02-19T04:06:04.054386Z",
                "is_edited": true,
                "date_edited": "2021-02-19T04:11:15.009832Z",
                "attachment": null,
                "total_likes": 0
            },
            {
                "id": 2,
                "comment": "This is my first comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 2,
                "post_text": "This is my updated second post. Hope you like it too!",
                "date_created": "2021-02-19T04:06:11.572011Z",
                "is_edited": false,
                "date_edited": null,
                "attachment": null,
                "total_likes": 0
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "No comment found. Make sure you are the author of the comment."
    }
    ```
#### Delete Comment API
- URL endpoint: api/feed/delete-comment/<comment_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "id": 4,
        "post": "This is a post for the app! Like it, if you like it.",
        "date_created": "2021-02-19T03:53:37.831118Z",
        "is_edited": true,
        "date_edited": "2021-02-19T03:53:25Z",
        "author": {
            "id": 3,
            "email": "abcdkaykobadreza@gmail.com",
            "first_name": "Kaykobad",
            "last_name": "Reza",
            "country": "",
            "language": "",
            "religion": "",
            "avatar": null
        },
        "total_likes": 0,
        "total_comments": 2,
        "attachment": null,
        "post_privacy": "friends",
        "comments": [
            {
                "id": 3,
                "comment": "This is my first comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 4,
                "post_text": "This is a post for the app! Like it, if you like it.",
                "date_created": "2021-02-19T04:06:26.529876Z",
                "is_edited": false,
                "date_edited": null,
                "attachment": null,
                "total_likes": 0
            },
            {
                "id": 4,
                "comment": "This is my first comment for testing.",
                "author": {
                    "id": 1,
                    "email": "admin@admin.com",
                    "first_name": "",
                    "last_name": "",
                    "country": "",
                    "language": "",
                    "religion": "",
                    "avatar": null
                },
                "post_id": 4,
                "post_text": "This is a post for the app! Like it, if you like it.",
                "date_created": "2021-02-19T04:06:30.355880Z",
                "is_edited": false,
                "date_edited": null,
                "attachment": null,
                "total_likes": 0
            }
        ]
    }
    ```
    or
    ```json
    {
        "detail": "Error! No comment found. Make sure you are the author of the comment and try with a valid comment id."
    }
    ```
#### Like Comment API
- URL endpoint: api/feed/like-comment/<comment_id>/
- Authentication required: True
- Request method: POST
- Request: None
- Response:
    ```json
    {
        "detail": "Success! You liked/unliked the comment."
    }
    ```
      or
    ```json
    {
        "detail": "Error! No comment found. Try with a valid comment id."
    }
    ```
  