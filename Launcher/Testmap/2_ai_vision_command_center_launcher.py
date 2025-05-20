import os
import time
import webbrowser

# Configuration
heal_the_world_project_folder = "L:/Heal the World Project"
suno_folder = "L:/ai_vision_command_center/SunoMusic"
youtube_folder = "L:/AI_Visionairy/YouTubeVideos"
author_folder = "L:/AI_Visionairy/Author"
default_browser = "https://www.google.com"

def make_folders():
    os.makedirs(heal_the_world_project_folder, exist_ok=True)
    os.makedirs(suno_folder, exist_ok=True)
    os.makedirs(youtube_folder, exist_ok=True)
    os.makedirs(author_folder, exist_ok=True)

def welcome():
    print("🌟 Welcome to AI Vision Command Center, Brigitte!")
    print("Let’s Make this World a Beautiful Place... 🔮")
    time.sleep(1)

def show_menu():
    print("\nChoose an option:")
    print("1. Open Heal the World Project")
    print("2. Open Suno Music Folder")
    print("3. Open YouTube Storage")
    print("4. Open Author Folder")
    print("5. Launch Google")
    print("6. Exit")

def run():
    make_folders()
    welcome()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            os.startfile(heal_the_world_project_folder)
        elif choice == "2":
            os.startfile(suno_folder)
        elif choice == "3":
            os.startfile(youtube_folder)
        elif choice == "4":
            os.startfile(author_folder)
        elif choice == "5":
            webbrowser.open(default_browser)
        elif choice == "6":
            print("Goodbye, Brigitte! ✨")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    run()
