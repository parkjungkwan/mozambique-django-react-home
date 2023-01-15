import axios, { AxiosResponse } from 'axios'
import {context} from '@/components/admin/enums'
import { currentTime } from '@/components/admin/utils'
import { User } from '@/modules/types'

export const user = {
    async join(payload: User){
            try{
                alert(`payload is ${JSON.stringify(payload)}`)
                const response : AxiosResponse<any, User[]> =
                await axios.post(`http://localhost:8000/users/register`, payload, {headers: {
                    "Content-Type" : "application/json",
                    Authorization: "JWT fefege...",
                }})
                if(response.data === "failure"){
                    alert(' 결과: API 내부 join 실패  ')
                }else{
                    alert(' 결과: API 내부 join 성공  '+ JSON.stringify(response.data))
                }
                
                return response
            }catch(err){
                console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
            }
        },
    async login(payload: User){
        try{
            alert(`payload is ${JSON.stringify(payload)}`)
            const url = `http://localhost:8000/users/login`
            alert(`url is ${url}`)
            const response : AxiosResponse<any, User[]> =
            await axios.post(url, payload)
            alert(` 서버에서 리턴받은 값: ${JSON.stringify(response.data)}`)
            localStorage.setItem("loginUser", JSON.stringify(response.data))
            //return response.data
        }catch(err){
            return err;
        }
    }
    
}
