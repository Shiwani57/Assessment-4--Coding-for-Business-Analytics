import pandas as pd

# Hypothetical data samples
data_articles = {
    'article_id': ['010101001', '010101002', '010102001'],
    'product_type': ['T-shirt', 'Pants', 'Dress'],
    'price': [9.99, 19.99, 29.99]
}
articles = pd.DataFrame(data_articles)

data_customers = {
    'customer_id': ['C001', 'C002', 'C003'],
    'age': [25, 35, 45],
    'membership_level': ['Silver', 'Gold', 'Platinum']
}
customers = pd.DataFrame(data_customers)

data_transactions = {
    'transaction_id': ['T001', 'T002', 'T003'],
    'customer_id': ['C001', 'C002', 'C003'],
    'article_id': ['010101001', '010101002', '010102001'],
    'date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'quantity': [1, 2, 1]
}
transactions = pd.DataFrame(data_transactions)



# Merge transactions with articles to include price information
merged_data = pd.merge(transactions, articles, on='article_id')
merged_data['total_sales'] = merged_data['quantity'] * merged_data['price']

# Group by product type to see total sales per product
sales_per_product = merged_data.groupby('product_type').sum()['total_sales']


import matplotlib.pyplot as plt

sales_per_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales per Product Type')
plt.xlabel('Product Type')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.show()
