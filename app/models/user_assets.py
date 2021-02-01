import app.repositories.user_repository as user_repository

current_user = user_repository.select_all()[0]