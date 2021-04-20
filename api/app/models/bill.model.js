const mongoose = require("mongoose");
const collectionName = 'bill';

const Bill = mongoose.model(
  "Bill",
  new mongoose.Schema({
    bill_id: String,
    user_id: String,
    amount: Number,
    description: String,
    isPaid: Boolean,
    contact: String
  })
  ,collectionName
);

module.exports = Bill;