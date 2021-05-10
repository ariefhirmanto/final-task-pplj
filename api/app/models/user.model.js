const mongoose = require("mongoose");
const collectionName = 'users';

const User = mongoose.model(
  "User",
  new mongoose.Schema({
    username: String,
    unique_id: String,
    email: String,
    password: String,
    name: String,
    roles: [
      {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Role"
      }
    ],
    amount_credit: Number,
    bill_id: [String],
    contact: String
  },
  { timestamps: true })
  ,collectionName
);

module.exports = User;