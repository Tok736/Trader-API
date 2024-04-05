from sqladmin import Admin, ModelView

from .app import app
from .db import engine
from .models import User, Product, Lesson

admin = Admin(app, engine)

class ProductModelView(ModelView, model=Product):
    column_list = [Product.id, Product.name, Product.created_at]
    form_excluded_columns = [Product.created_at, Product.updated_at]

class LessonModelView(ModelView, model=Lesson):
    column_list = [Lesson.id, Lesson.name, Lesson.created_at]
    form_excluded_columns = [Lesson.created_at, Lesson.updated_at]

class UserModelView(ModelView, model=User):
    column_list = [User.id, User.name, User.created_at, User.avatar_image]
    form_excluded_columns = [User.created_at, User.updated_at]

admin.add_view(ProductModelView)
admin.add_view(LessonModelView)
admin.add_view(UserModelView)
