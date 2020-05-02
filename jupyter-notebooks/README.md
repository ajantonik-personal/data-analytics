# Jupyter Notebooks

### [spotify_api_artist_search](/jupyter-notebooks/spotify_api_artist_search.ipynb)
#### Purpose
Search the Spotify API for artists and retrieve their metadata. Then, classify artists by their genres, and determine other artists to recommend based on genre similarity.

#### Implementation
The user can choose to enter artists manually in the notebook or populate an artist list in [spotify_artists.txt](/jupyter-notebooks/config/spotify_artists.txt) for which the analysis will be performed.

The user can also choose whether to have artists recommended. If not, only the metadata and initial genre classification of the artists selected will be output.

Once parameters are set, the notebook authenticates Spotify API credentials (stored locally & acceessed via environment variable). 

It then extracts metadata from the Spotify API artist search route and stores it in a dataframe. From there, the list of genres for each artist is compared against the full list of sub-genres maintained by [Every Noise at Once](http://everynoise.com/engenremap.html), and a resulting boolean dataframe is generated. This is then used to determine genre similarities between artists and return artist recommendations based on the number of sub-genres in-common.

#### Examples

[All Artists From File](/jupyter-notebooks/spotify_api_artist_search_example_all.ipynb)

[Manually Selected Artists](/jupyter-notebooks/spotify_api_artist_search_example_manual.ipynb)

#### TODOs
1. Support export of results to Postgres
2. Run initial metadata extraction and genre classification for all artists on Spotify and store in Postgres to be accessed on the fly in subsequent runs
3. Categorize all sub-genres into genre themes, and re-tool artist recommendations based on % similarity within and between themes (rather than absolute similarity within sub-genres)
