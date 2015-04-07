var Wheel = require('./Wheel.react.jsx');
var React = require('react');

var Car = React.createClass({

  render: function() {
    return (
      <div className="car">
        A car with the following wheels
        <ul>
          <li>
            <Wheel />
          </li>
          <li>
            <Wheel />
          </li>
          <li>
            <Wheel />
          </li>
          <li>
            <Wheel />
          </li>
      </ul>
      </div>
    );
  }

});

module.exports = Car;
