import React from 'react';
import ReactDOM from 'react-dom';



class Input extends React.Component {

    constructor(props) {
        super(props);
    
        this.state = {
            input_field: '',
            items: [],
            isLoaded: false
        };
    }

    componentDidMount () {

        fetch('http://api.openweathermap.org/data/2.5/weather?zip=98119&appid=65036b8d41536ad067f7d3079698ebcc')
            .then(res => res.json())
            .then(json => {
                console.log(json)
                this.setState({
                    isLoaded: true,
                    items: json.weather,
                })
            });
    }

    update(event) {
        this.setState({

        })
    }

    render() {

        var {isLoaded, items} = this.state;

        if (!isLoaded) {
            return (
            <div>Loading...</div>
            )
        } else {
            return React.createElement('ul', {}, items.map(item => 
                React.createElement('li')))
            return (
                <ul>
                    {items.map(item => (
                        <li key={item.id}>
                            {item.main}
                        </li>
                    ))}
                </ul>
            )
        }

        /* return(
            <div>
                <h4>It's weather time!</h4>
                <input type='text'
                value= {this.state.item_input}
                onChange = {this.update} />
                <button type = 'button'
                onClick={this.add}>Search</button>
            </div>
        ) */
    }
}

  ReactDOM.render(
    <Input />,
    document.getElementById('root')
  );
  