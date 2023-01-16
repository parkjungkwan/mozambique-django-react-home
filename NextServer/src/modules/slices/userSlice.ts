import { createSlice, PayloadAction, createSelector } from "@reduxjs/toolkit"
import { User } from '@/modules/types'
import { AppState } from "../store";
type UserState = {
    data: User[]
    status: 'idle' | 'loading' | 'failed'
    isLoggined: boolean
    error: any,
    token: string
}
const initialState: UserState = {
    data: [],
    status: 'idle',
    isLoggined: false,
    error: null,
    token: "test"
}

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        joinRequest(state: UserState, action: PayloadAction<User>){
            state.status = 'loading'
            state.error = null
        },
        joinSuccess(state: UserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        joinFailure(state: UserState, {payload}){
            state.status = 'failed'
            state.data = [...state.data, payload]
        },
        loginRequest(state: UserState, _payload){
            state.status = 'loading'
        },
        loginSuccess(state: UserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        loginFailure(state: UserState, {payload}){
            state.status = 'failed'
            state.data = [...state.data, payload]
        },
        logoutRequest(state: UserState) {
            state.status = 'loading';
            state.error = null;
        },
        logoutSuccess(state: UserState ){
            state.status = 'idle'
            window.location.href = '/'
        },
        logoutFailure(state: UserState, action: PayloadAction<{ error: any }>) {
            state.status = 'failed';
            state.error = action.payload;
        },

        // 회원정보
        setUserInfo(state: UserState) {
            state.status = 'idle';
            state
        }

    }
})

const {reducer, actions} = userSlice
export const {joinRequest, joinSuccess, joinFailure,
            loginRequest, loginSuccess, loginFailure,
            logoutRequest, logoutSuccess, logoutFailure
} = userSlice.actions
export const userAction = actions
export default reducer
/** 
interface Reply{
    id: number,
    comment: string,
    count: number
}

const initialState2: Reply = { // 여기 초기값이 선언되어있다. 
    id : 5,
    comment : 'test',
    count : 199
  };

  
  export const countSelector = (state: AppState): number =>   // 카운트를 저장
    state.reply.count || initialState2.count;   // 값이 있으면 사용하고 아니면 초기값을 가져다 쓴다
  
  export const commentSelector = (state: AppState): string => // 코멘트를 저장
    state.reply.comment || initialState2.comment;
  
  export const replySelector = createSelector( // 위에서 저장한 데이터를 찐 셀렉터로 만들어주자
    countSelector,			     // 각각의 셀렉터들을 넣고
    commentSelector,
    (count, comment) => ({ 	 // 마지막 인자로 함수를 넣는데 state 자체를 인자로 넣고, 
        count, comment 		 // 리턴받을 데이터를 넣어준다 (filter나 계산식 등으로 가공해도 된다)
    }) 
  );

 */
export const dataSelector = (state: AppState): [] => state.user.data || initialState.data;

export const tokenSelector = (state: AppState): string => state.user.token || initialState.token;

export const userSelector = createSelector(
    dataSelector,
    tokenSelector,
  (data, token) => {
    return `My Data is ${data}. token is ${token} `;
  }
);
       