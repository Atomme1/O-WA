# This query gets a lot of information from all events of tournaments
# Anthology : tournament -> events -> phases (or in other terms pools like "Pool A1")
tournament_query_by_slug_heavy = """
  query GetTournamentInfo($tourneySlug: String!) {
    tournament(slug: $tourneySlug) {
      id
      name
      slug
      shortSlug
      numAttendees
      startAt
      events {
        id
        slug
        name
        numEntrants
        videogame {
          id
          displayName
          slug
        }
        phases {
          id
          name
          phaseGroups(query: { page: 1, perPage: 100 }) {
            nodes {
              id
              displayIdentifier
            }
          }
        }
      }
    }
  }
"""

# This query gets sets from a phase group
# So if you want to get the sets from group A1 you need to input the ID of this group.
# There will always be a phase group even if your tournament only have one tree, so you can always use this to get sets
# from an event
sets_query_from_phaseGroup_from_phase = """
  query PhaseGroupSets($phaseId: ID!, $page: Int!){
    phaseGroup(id: $phaseId){
      sets(page: $page, perPage: 100, sortType: STANDARD) {
        pageInfo {
          totalPages
        }
          nodes {
            id
            fullRoundText
            identifier
            slots {
              entrant {
                id
                name
              }
            }
         }
      }
    }
  }
"""