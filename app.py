from flask import Flask, render_template, request
from products import search,price_comparison
# from googlesearch import search

from user_agent import search_for_product,final_result

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
async def search_results():
    product_name = request.form.get('product_name')

    await search_for_product(product_name)
    print(final_result)
    
    
    # results = search(product_name)

    if final_result:
        return render_template('results.html', query=product_name, results=price_comparison(product_name))
    else:
        return render_template('not_available.html',query=product_name)
        

if __name__ == '__main__':
    app.run(debug=True)
