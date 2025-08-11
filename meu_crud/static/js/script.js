function confirmarExclusao(nome, url) {
    if (confirm(`Tem certeza que deseja excluir "${nome}"?`)) {
        window.location.href = url;   
    }
}

function mostrarMensagemAcao() {
    const urlParams = new URLSearchParams(window.location.search);
    const acao = urlParams.get('acao');
    
    if (acao) {
        switch(acao) {
            case 'criar':
                alert('Registro criado com sucesso!');
                break;
            case 'editar':
                alert('Registro editado com sucesso!');
                break;
            case 'excluir':
                alert('Registro excluído com sucesso!');
                break;
        }
        window.history.replaceState({}, document.title, window.location.pathname);
    }
}

window.onload = mostrarMensagemAcao;