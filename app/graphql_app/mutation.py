import strawberry

from app.graphql_app.resolvers import chores, zones

@strawberry.type
class Mutation:

        #get zone info
        set_zones_quick_view = strawberry.field(resolver=zones.set_zones_quick_view)


        # chores
        start_record_task_time = strawberry.field(resolver=chores.start_record_task_time)
        end_record_task_time = strawberry.field(resolver=chores.end_record_task_time)