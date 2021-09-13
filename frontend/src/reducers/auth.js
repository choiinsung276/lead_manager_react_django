const initialState ={
    token: localStorage.getItem('token'),
    isAuthenticated: null,
    isLoading: false,
    user: null
}
//create function
export default function (state = initialState, action){
    switch (action.type){
        default:
            return state;
    }
}