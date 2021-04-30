query anime($anime: String) {
  Media(search: $anime, sort: SEARCH_MATCH, type: ANIME) {
    title {
      userPreferred
      romaji
    }
    description (asHtml: false)
    siteUrl
    averageScore
    status
    episodes
    genres
    coverImage {
      large
      color
    }
  }
}
