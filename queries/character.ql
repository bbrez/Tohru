query character($char: String) {
  Character(search: $char, sort: SEARCH_MATCH) {
    name {
      full
      native
      alternative
      alternativeSpoiler
    }
    favourites
    image {
      large
    }
    siteUrl
    description
  }
}