from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
 
# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World!')

def index_template(request):
    return render(request, 'index.html')

from gensim.models import word2vec

def ret_ans(actor):
    """
    選択された監督俳優のモデルから演算結果を渡す関数
    modelのファイルどこに置こう。
    """
    if actor=='d':
        voc = 'ドゥニ・ヴィルヌーヴ'
        model = word2vec.Word2Vec.load('/home/runa/git/moviesWord2vec/somePlusMoviesSite/helloworld/denis.model')
    else:
        voc = ''
        model = 'some'

    out = model.most_similar(positive=[voc, '映画'], topn = 10)
    return out

from .forms import MyForm
from .forms import ActorForm

def form_test(request):
    if request.method == "POST":
        form = ActorForm(data=request.POST)  # ← 受け取ったPOSTデータを渡す
        if form.is_valid():  # ← 受け取ったデータの正当性確認
            # pass  # ← 正しいデータを受け取った場合の処理
            return render(request, 'helloworld/form.html', {
                'form' : form,
                #'choice' : request.POST['actor'],
                'choice' : ret_ans(request.POST['actor'])
            })
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        form = ActorForm()
    return render(request, 'helloworld/form.html', {
        'form': form,
    })


#def form_test(request):
    #form = MyForm()
#    form = ActorForm()
#    return render(request, 'helloworld/form.html', {
#        'form': form,
#    })
