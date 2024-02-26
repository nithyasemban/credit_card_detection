from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/check_fraud', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        year = int(request.form['year'])
        month = int(request.form['month'])
        use_chip = int(request.form['use_chip'])
        amount = int(request.form['amount'])
        merchant_name = request.form['merchant_name']
        merchant_city = request.form['merchant_city']
        merchant_country = request.form['merchant_country']
        mcc = int(request.form['mcc'])

        # Process the form data as needed (you can store it in a database, etc.)

        # For now, just print the data to the console
        print(f"Year: {year}, Month: {month}, UseChip: {use_chip}, Amount: {amount}, "
              f"MerchantName: {merchant_name}, MerchantCity: {merchant_city}, "
              f"MerchantCountry: {merchant_country}, MCC: {mcc}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
