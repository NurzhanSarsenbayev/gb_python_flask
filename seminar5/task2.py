# Задание №2
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.
from typing import Optional, List

from fastapi import FastAPI,Query,HTTPException
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str]
    genre: str

app = FastAPI()
movies = [
    Movie(id=1, title="Inception", description="A thief who steals corporate secrets through the use of dream-sharing technology.", genre="Sci-Fi"),
    Movie(id=2, title="The Godfather", description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", genre="Crime"),
    Movie(id=3, title="Toy Story", description="A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", genre="Animation"),
    Movie(id=4, title="Pulp Fiction", description="The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.", genre="Crime"),
    Movie(id=5, title="Interstellar", description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", genre="Sci-Fi"),
]

@app.get("/movies", response_model=List[Movie])
async def get_movies_by_genre(genre: str = Query(..., description="The genre to filter movies by")):
    genre_movies = [movie for movie in movies if movie.genre.lower() == genre.lower()]
    if not genre_movies:
        raise HTTPException(status_code=404, detail="No movies found for this genre")
    return genre_movies

# Маршрут для получения списка всех фильмов (без фильтрации)
@app.get("/movies/all", response_model=List[Movie])
async def get_all_movies():
    return movies