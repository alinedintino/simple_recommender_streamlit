import scipy
import pickle
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import constants as const
from script.utils import get_recommendations


def weighted_average_based_recommendations():
    """read saved df sorted based on scores
    and get top movies"""
    with open('data/movie_scores.pickle', 'rb') as handle:
        movies = pickle.load(handle)
    movies = movies.head(const.MOVIE_NUMBER)
    movies = movies[["id", "title", "score"]]
    movies.columns = ["movieId", "title", "score"]
    return movies


def contend_based_recommendations(movie, titles):
    """read and call similarity function"""
    tfidf_matrix = scipy.sparse.load_npz('data/tfidf_matrix.npz')
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return get_recommendations(movie, titles, cosine_sim)



