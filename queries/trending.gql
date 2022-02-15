query trend($pp: Int){
  Page(perPage: $pp) {
    media(sort: TRENDING_DESC, type: ANIME){
      title {
        userPreferred
      }
      siteUrl
      coverImage {
        extraLarge
        color
      }
    }
  }
}