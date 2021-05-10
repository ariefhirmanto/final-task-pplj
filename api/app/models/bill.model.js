const mongoose = require("mongoose");
const collectionName = 'bill';

const Bill = mongoose.model(
  "Bill",
  new mongoose.Schema({
    bill_name: String,
    bill_id: String,
    bill_owner: String,
    bill_sender: String,
    amount: Number,
    description: String,
    isPaid: Boolean
  },
  { timestamps: true })
  ,collectionName
);

module.exports = Bill;