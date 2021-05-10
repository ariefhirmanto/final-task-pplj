const mongoose = require("mongoose");
const collectionName = 'transfers';

const Transfer = mongoose.model(
  "Transfer",
  new mongoose.Schema({
    username: String,
    change_balance: Number,
    category: String
  },
  { timestamps: true })
  ,collectionName
);

module.exports = Transfer;