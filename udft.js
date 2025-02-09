function transformSalesData(inJson) {
    var obj = JSON.parse(inJson);
    /* Create new object */
    var obj1 = new Object();

    /* Map string object elements to string variables */
    var strTransactionId = obj.transaction_id;
    var strProductId = obj.product_id;
    var numQuantity = obj.quantity;
    var numSalesAmount = obj.sales_amount;
    var numTimestamp = obj.timestamp;

    /* Create calculated fields */
    var numTotalValue = numQuantity * numSalesAmount;
    var strFormattedTimestamp = new Date(numTimestamp * 1000).toISOString();

    /* Map string variables to new object elements */
    obj1.transaction_id = strTransactionId;
    obj1.product_id = strProductId;
    obj1.quantity = numQuantity;
    obj1.sales_amount = numSalesAmount;
    obj1.timestamp = strFormattedTimestamp;
    obj1.total_value = numTotalValue;

    /* Return new object */
    return JSON.stringify(obj1);
}