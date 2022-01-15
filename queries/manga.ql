query manga($manga: String) {
  Media(search: $manga, sort: SEARCH_MATCH, type: MANGA) {
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
