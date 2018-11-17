# MLModel Class

The only customisation required for this class is the `predict` method.
You can either use any one of Random Forest or Support Vector Machine (SVM) or a combination of both models.

A possible way in which both models are used together would be to let both Random Forest and SVM predict
the dance move; and only return the result when both models predict the same dance move.

Note that `MLModel` class is only used during real time prediction of dance moves.
