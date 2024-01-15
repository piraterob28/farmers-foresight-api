import strawberry

from app.graphql_app.resolvers import zones

@strawberry.type
class Mutation:

        #get zone info
        set_zones_quick_view = strawberry.field(resolver=zones.set_zones_quick_view)