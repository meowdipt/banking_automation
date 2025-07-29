CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    doc_number VARCHAR(50) NOT NULL,
    doc_date DATE NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    supplier VARCHAR(100),
    recipient VARCHAR(100),
    doc_type VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_doc_number ON documents(doc_number);
CREATE INDEX idx_doc_date ON documents(doc_date);