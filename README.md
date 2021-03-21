# OnlineTreasureHunt

 The app allows you to play an OnlineTreasureHunt consisting of different levels.Players can login either using their <code>Google</code> or </code>Facebook</code> accounts. Each level has a question and hints along with it like **visual hints**, **audio hints**, **video hints** .Each question would fetch you 10 points. Once the player answers the question the leaderboard is updated accordingly.
  


##  Setting up the Project


1. Create a </code>virtual environment</code> .

    mkdir project

    cd project
    ```
    python3 -m venv venv
    ```

2. Clone the project in the project directory.

    git clone https://github.com/nirvikagarwal/OnlineTreasureHunt.git

    ```
3. Activate the virtual environemnt.
    #### For Linux/Mac OSX   
    ```
    source venv/bin/activate

    ```
    #### For Windows
    ```
    .\Scripts\activate

    ```
4. Install the requirements.
    ```
    cd OnlineTreasureHunt
    pip install -r requirements.txt

    ```
5. Go to the path   venv/lib/django/contrib/auth/urls.py.

    after all the import statements add <code>app_name='auth'</code> on the next line

6. Set the environment variables

    ```
    cp .env.example .env
    ```
    Add the corresponding values in the .env file and save it
   
7. Run the Migrations
    ```
    python manage.py makemigrations

    python manage.py migrate

    ```
8. Create Superuser
    ```
    python manage.py createsuperuser
    ```
9. Run the development server
    ```
    python manage.py runserver

    ```
10. Head over to http://localhost:8000/admin and login as super user

11. Add config and some levels to begin with.

12. Now you can login with your <code>Google</code> / </code>Facebook</code> account and enjoy the game


![image](https://github.com/kgulshan827/OnlineTreasureHunt/blob/master/pic.png)
