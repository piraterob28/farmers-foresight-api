import strawberry

from app.graphql_app.resolvers import chores, zones


@strawberry.type
class Query:

    # get zone info
    get_zones_quick_view = strawberry.field(resolver=zones.get_zones_quick_view)


    # get TaskListView info

    # Chores
    get_chore_list_one_zone = strawberry.field(resolver=chores.get_chore_list_one_zone)

