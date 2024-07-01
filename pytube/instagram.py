import instaloader
from instaloader.exceptions import ProfileNotExistsException, BadResponseException, LoginRequiredException, ConnectionException

def download_instagram_profile_picture(username, insta_username, insta_password):
    insta = instaloader.Instaloader()

    try:
        # Login
        insta.login(insta_username, insta_password)

        print(f"Downloading profile picture for user: {username}")
        insta.download_profile(username, profile_pic_only=True)
        print("Download complete!")
    except ProfileNotExistsException:
        print(f"Error: The profile '{username}' does not exist.")
    except BadResponseException:
        print("Error: Failed to connect to Instagram. Please check your internet connection.")
    except LoginRequiredException:
        print("Error: Login required. Please check your username and password.")
    except ConnectionException:
        print("Error: Failed to connect to Instagram. Please check your internet connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    user = input("Enter the Instagram username to download the profile picture: ")
    insta_username = input("Enter your Instagram username: ")
    insta_password = input("Enter your Instagram password: ")
    download_instagram_profile_picture(user, insta_username, insta_password)
