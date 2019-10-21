/*jshint esversion: 6 */

import React from 'react';
import ReactDOM from 'react-dom';
import Request from 'superagent';
import _ from 'lodash';


class Input extends React.Component {

    constructor() { 
        super();
        this.state = {
            zip: 98119
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
        if (!this.state.weather) {
            return <div>
            <input ref="query" type="text" />
            <button onClick={ (e) => {this.clicked(); }}>Search</button>
            </div>
        }

        var temp = this.state.weather.main.temp
        temp = Math.floor(((temp - 273.15)*9/5 + 32))
        console.log(temp)

        return <div>
            <input ref="query" type="text" />
            <button onClick={ (e) => {this.clicked(); }}>Search</button>
            <pre>{ JSON.stringify(this.state.weather) }</pre>
            <h4>{ this.state.weather.weather[0].description }</h4>
            <h4>{temp} F</h4>

            
        </div>
    }

    search(query = "98119") {
        var url = `http://api.openweathermap.org/data/2.5/weather?zip=${query}&appid=65036b8d41536ad067f7d3079698ebcc`;
        Request.get(url).then((response) => {
            console.log(response.body.name);
            this.setState({
                weather: response.body
            });
        });
        
    }
}

  ReactDOM.render(
    <Input />,
    document.getElementById('root')
  );