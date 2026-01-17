from trulens_eval import Feedback
from trulens_eval.feedback.provider.groq import Groq
from trulens_eval.feedback import AnswerRelevance, Groundedness

provider = Groq()

relevance = Feedback(
    AnswerRelevance(provider).measure
)

groundedness = Feedback(
    Groundedness(provider).measure
)