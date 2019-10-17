/*jshint esversion: 6 */

import React from 'react';
import ReactDOM from 'react-dom';
import Request from 'superagent';
import _ from 'lodash';


class Input extends React.Component {

    constructor() { 
        super();
        this.state = {
            zip: 98119,
            dict: {}
        };
    }

    componentWillMount () {
        this.search();
    }

    updateSearch () {
        this.search(this.refs.query.value);
    }

    clicked () {
        this.setState({
            zip: this.refs.query.value
        });
        this.search(this.refs.query.value);
    }

    render() {
        //var weatherArr =  ? [this.state.weather.loc, this.state.temp] : []
        var weather = (dict) ? _.map(weatherArr, (json) => {
            //var temperature = {json.main.temp};
            //var far = ((temperature − 273.15) × 9/5 + 32);
            return <div>
            <li>{ json.loc }</li>
            <li>{ json.temp }</li>
            </div>
        }) : 
            return <div></div>
        return <div>
            <input ref="query" type="text" />
            <button onClick={ (e) => {this.clicked(); }}>Search</button>
            <ul>{ weather }</ul>
        </div>
    }

    search(query = "98119") {
        var url = `http://api.openweathermap.org/data/2.5/weather?zip=${query}&appid=65036b8d41536ad067f7d3079698ebcc`;
        Request.get(url).then((response) => {
            console.log(response.body.name);
            this.setState({
                weather: response.body,
                loc: response.body.name,
                temp: response.body.temp,
                dict: {
                    loc: weather.name,
                    temp: weather.temp
                }
            });
        });
        
    }
}

  ReactDOM.render(
    <Input />,
    document.getElementById('root')
  );
  