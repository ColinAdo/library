from pytest_factoryboy import register

from .factory import (
    CategoryFactory, 
    BookFactory, 
    ProgressFactory, 
    ReviewFactory,

    CustomUserFactory,

    )

register(CategoryFactory)
register(BookFactory)
register(ProgressFactory)
register(ReviewFactory)

######################################## userAuths app ########################################################
register(CustomUserFactory)