import React from 'react'
import { useNavigate } from 'react-router-dom';

export function StartPageRouterComponent() {

    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/clients')
    };

    return (
        <button onClick={handleClick}>Переход</button>
    )
}