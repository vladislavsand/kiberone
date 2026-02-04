import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import { StartPageComponents } from './StartComponents/StartPage'; 
import { ClientsPageComponent } from './ClientsPageComponents/ClientsPage';

// function App() {
//   return (
//     <div className="App">
//       <LoginPage/>
//     </div>
//   );
// }

function App(props) {
      return (
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<StartPageComponents />} />
            <Route path="/clients" element={<ClientsPageComponent />} />
          </Routes>
        </BrowserRouter>
      );
    }

export default App;
