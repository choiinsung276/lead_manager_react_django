import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Header from './layout/Header';
import Dashboard from "./leads/Dashboard";
import Alerts from "./layout/Alerts";
import Leads from "./leads/Leads";
import Form from "./leads/Form";

import {Provider as AlertProvider} from 'react-alert';
import { Provider} from "react-redux";
import store from '../store';


import AlertTemplate from "react-alert-template-basic";

// Alert Options
const alertOptions = {
    timeout: 3000,
    position: 'top center'
}

class App extends Component{
    render() {
        return (
            <Provider store={store}>
            <AlertProvider template={AlertTemplate} {...alertOptions}>
            <Fragment>
                <Header />
                <Alerts />
                <div className="container">
                    <Dashboard />
                </div>
            </Fragment>
            </AlertProvider>
            </Provider>
            );
    }
}

ReactDOM.render(<App />, document.getElementById('app'));