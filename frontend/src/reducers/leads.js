// GET_LEADS 라는 types
import {DELETE_LEAD, GET_LEADS, ADD_LEAD} from '../actions/types.js';

// 초기 state
const initialState = {
    //something:'text',
    leads: []
}

export default function (state= initialState, action ) {
    switch (action.type){
        case GET_LEADS:
            return {
                ...state,
                leads: action.payload
            };
        case DELETE_LEAD:
            return {
                ...state,
                leads: state.leads.filter(lead => lead.id !==
                action.payload)
            }
        case ADD_LEAD:
            return {
                ...state,
                leads: [...state.leads, action.payload]
            };
        default:
            return state;
    }
}