const db = require("../models");
const Bill = db.bill;

exports.findAll = (req, res) => {
  Bill.find()
    .then(data => {
        res.send(data);
    }).catch(err => {
        res.status(500).send({
            message: err.message || "Some error occurred while retrieving notes."
        });
    });
};

// Find a single Bill with an id
exports.findOne = (req, res) => {  
  Bill.find({ Bill_id: req.params.Bill_id })
  .then(data => {
      if(!data) {
          return res.status(404).send({
              message: "Bill not found " + req.params.Bill_id
          });            
      }
      res.send(data);
  }).catch(err => {
      if(err.kind === 'ObjectId') {
          return res.status(404).send({
              message: "Bill not found with id " + req.params.Bill_id
          });                
      }
      return res.status(500).send({
          message: "Error retrieving Bill with id " + req.params.Bill_id
      });
  });
};


