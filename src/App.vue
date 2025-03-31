<script>
import axios from 'axios';

export default {
  data(){
    return {
      searchTerm: '',
      results: []
  };
},
  methods: {
    async search() {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/buscar`, {
          params: { q: this.searchTerm}
        });
        this.results = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  }
};
</script>

<template>
  <div id="app">
    <div class="container">
      <h1>Teste de API</h1>
      <form @submit.prevent="search">
        <input type="text" v-model="searchTerm" placeholder="Digite sua pesquisa" />
        <button type="submit">Pesquisar</button>
      </form>
      <ul>
        <li v-for="resultado in results" :key="resultado.id">
          <h3>Registro_ANS: {{ resultado.Registro_ANS }}</h3>
          <p>CNPJ: {{ resultado.CNPJ }}</p>
          <p>Razão Social: {{ resultado.Razao_Social }}</p>
          <p>Cidade: {{ resultado.Cidade }}</p>
          <p>UF: {{ resultado.UF }}</p>
          <p>Endereço Eletronico: {{ resultado.Endereco_eletronico }}</p>
          <p>Telefone: {{ resultado.DDD }}-{{ resultado.Telefone }}</p>
          <p>Representante: {{ resultado.Representante }} Cargo: {{ resultado.Cargo_Representante }}</p>
          <p>Logradouro: {{ resultado.Logradouro }}</p>
          <p>CEP: {{ resultado.CEP }}</p>
          
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
  }

  form {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
  }

  input {
    padding: 10px;
    margin-right: 10px;
    width: 500px;
  }

  button {
    padding: 10px 20px;
    background-color: #42b983;
    color: white;
    border: none;
    cursor: pointer;
  }

  ul {
    padding: 0;
  }

  li {
    list-style: none;
    margin: 10px 0;
    padding: 10px;
    background-color: #333;
    border-radius: 5px;
    text-align: left;
  }
</style>