import { combineReducers} from "redux";
import leads from './leads';
import errors from "./errors"
import messages from "./messages";
import auth from "./auth"
export default combineReducers({
    leads,
    errors,
    messages,
    auth
    // leadReducer : leads 같이 쓰는데 일단은 그냥 leads파일 만 부를땐 leads
});