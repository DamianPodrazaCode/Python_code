import torch
from torch import nn 

loss_fn = nn.L1Loss() # Regresja. Tworzy kryterium, które mierzy średni błąd bezwzględny (MAE) 
                      # między każdym elementem w danych wejściowych X i docelowych y.

loss_fn = nn.MSELoss() # Regresja. Tworzy kryterium, które mierzy średni błąd kwadratowy (norma kwadratowa L2) 
                       # między każdym elementem na wejściu X i celem y. 

loss_fn = nn.CrossEntropyLoss() # Klasyfikacja wieloklasowa. Stosuje się gdy mamy więcej wyjść, oblicza prawdopodobieństwo przynależności do wyjścia,
                                # np. Uczymy sieć że mamy 3 możliwości odpowiedzi, więc mamy 3 wyjścia, w odpowiedzi dostajemy 3 liczby, 
                                # najwyższa jest naszym największym przawdopodobieństwem odpowiedzi. Do dego stosujemy torch.softmax() 
                                # żeby znormalizować odpowieć tz. suma odpowiedzi będzie wynoaiła 1, np. y_out -> [1.2, 0.9, 0.4] 
                                # po softmax [0.46, 0.34, 0.2], odczytujemy przy pomocy torch.argmax() index najwyższej w tym przypadku pozycja 0, 
                                # i wiemy że największe prawdopodobieństo prawidłowej odpowiedzi to odpowiedz zerowa z trzech numerowanych 0,1,2
                                # dane wyjściowe muszą być typu torch.LongTensor, oczywiście odpowiedź 0.46 ma 46% szans na poprawność odpowiedzi
                                    
loss_fn = nn.CTCLoss() 
loss_fn = nn.NLLLoss() 
loss_fn = nn.PoissonNLLLoss() # regresja 
loss_fn = nn.KLDivLoss()
loss_fn = nn.BCELoss() # Klasyfikacja binarna

loss_fn = nn.BCEWithLogitsLoss() # Klasyfikacja binarna, y_out -> sigmoid -> round

loss_fn = nn.MarginRankingLoss()
loss_fn = nn.HingeEmbeddingLoss()
loss_fn = nn.MultiLabelMarginLoss()
loss_fn = nn.HuberLoss() # regresja 
loss_fn = nn.SmoothL1Loss() # regresja
loss_fn = nn.SoftMarginLoss() # Klasyfikacja binarna
loss_fn = nn.MultiLabelSoftMarginLoss()
loss_fn = nn.MultiMarginLoss()
loss_fn = nn.TripletMarginLoss()
loss_fn = nn.TripletMarginWithDistanceLoss()
