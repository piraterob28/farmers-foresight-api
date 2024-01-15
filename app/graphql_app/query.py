import strawberry

from app.graphql_app.resolvers import zones


@strawberry.type
class Query:

    # get zone info
    get_zones_quick_view = strawberry.field(resolver=zones.get_zones_quick_view)

