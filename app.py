# Import libraries
from flask import Flask, request, render_template, url_for, redirect

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation- we will access all the data in transactions
@app.route('/', methods=['GET'])
def get_transactions():
        return render_template("transactions.html", transactions=transactions)
    # try:
    #     if transactions and len(transactions) > 0:
    #         return {'message': f'{len(transactions)} transactions has been made'}, 200
    # except NameError:
    #     return {'message': 'an error occured'}, 404
    
@app.route('/count', methods=['GET'])
def get_count():
    if transactions:
        return {'message': f'{len(transactions)}'}, 200
    return {'message': 'no count'}, 404

# Create operation - create transaction based on the forms in template folder
@app.route('/add', methods=['POST', 'GET'])
def add_transaction():
    if request.method == 'POST':
        new_transaction = {
            'id':len(transactions) + 1,
            'date':request.form['date'],
            'amount':float(request.form['amount'])
        }
        transactions.append(new_transaction)
        # now lets redirect to the transactions list page
        return redirect(url_for('get_transactions'))
      # Render the form template to display the add transaction form
    return render_template("form.html")

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']
        amount = float(request.form['amount'])

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break

        # Redirect to the transactions list page
        return redirect(url_for("get_transactions"))
    
    # Find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)

# Delete operation
@app.route('/delete/<int:id>', methods= ['DELETE'])
def remove_transaction(id):
    for item in transactions[:]:
            if item['id'] == id:
             transactions.remove(item)
             break
            # now lets redirect to the transactions list page
            return redirect(url_for('get_transactions'))

# Ensure current script is the main programme
if __name__ == "__main__":
    app.run(debug=True)
    