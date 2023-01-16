import Link from "next/link"
import 'bootstrap/dist/css/bootstrap.css'
import { useDispatch, useSelector } from 'react-redux';
import { User } from "@/modules/types"
import { AppState } from "@/modules/store"
import {tokenSelector} from "@/modules/slices";
import {useAppSelector} from "@/modules/store";

export default function Navbar(){

  const token = useSelector(tokenSelector)

  console.log(` token is ${token}`)

  return (
    <div className="container-fluid">
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item"><Link href="/">홈</Link></li><span style={{width:10}}/>
        <li className="nav-item"><Link href="/counter">카운터</Link></li><span style={{width:10}}/>
        <li className="nav-item"><Link href="/user/join">회원가입</Link></li><span style={{width:10}}/>
        <li className="nav-item"><Link href="/user/login">로그인</Link></li><span style={{width:10}}/>
        <li className="nav-item"><Link href="/user/list" >사용자목록</Link></li><span style={{width:10}}/>
      </ul>
      </nav>

    </div>
  );
}

