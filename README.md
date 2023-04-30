
# Games - Your favorite steam games list

This web app is allowing you to easily manage your favorite games on steam. 


## Demo

Follow this link [https://games.michalpilarski17.smallhost.pl] to get to the demo


## Authors

- [@CarianS (Krzysztof Kasperek) ](https://github.com/Carians)
- [@Michal-Pilarski](https://github.com/Michal-Pilarski)

## Run Locally

Clone the project

```bash
  git clone https://github.com/Carians/Games.git
```

Go to the project directory

```bash
  cd Games
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Make migrations

```bash
  python manage.py makemigrations
```

Migrate migrations

```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
  ```

# API Reference

### Endpoints
```
GET /api/games
This endpoint returns a list of all games in the library as JSON.
```
```
POST /api/games
This endpoint creates a new game in the library.
```
```
GET /api/games/:id
This endpoint returns a single game from the library with the specified id as JSON.
```
```
PUT /api/games/:id/update
This endpoint updates a game in the library with the specified id.
```
```
DELETE /api/games/:id/delete
This endpoint deletes a game from the library with the specified id.
```
```
GET /api/gamesreview
This endpoint returns a list of all game reviews in the library as JSON.
``` 
```
POST /api/gamesreview
This endpoint creates a new game review in the library.
``` 
```
GET /api/gamesreview/:gameName
This endpoint returns all game reviews for the game with the specified gameName as JSON.
``` 
```
PUT /api/gamesreview/:gameName/update
This endpoint updates a game review for the game with the specified gameName.
``` 
```
DELETE /api/gamesreview/:gameName/delete
This endpoint deletes a game review for the game with the specified gameName.
``` 
```
GET /login
This endpoint displays the login page.
``` 
```
POST /login
This endpoint logs the user into the application.
``` 
```
GET /logout 
This endpoint logs the user out of the application.
``` 