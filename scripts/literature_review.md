# Literature Review Context

Date: 2026-05-16

## Objective

Create a reusable context note for the literature-review process carried out for the thesis topic:

`MTP 2: Limit Order Book - Framework for Market Making`

This file records:

- what was analyzed
- which files and papers were reviewed
- how the PDF-reading notebook works
- the main literature synthesis used for drafting
- the draft abstract and introduction produced from this review
- the bibliography entries prepared for direct use

## Important Context

- The thesis draft used for the writing task was pasted directly in chat by the user.
- The repository file `C:\GIT\r_proposal\main.tex` is a shorter research proposal, not the full thesis draft pasted in chat.
- The thesis draft pasted in chat was treated as the primary target document for the abstract and introduction.
- No project files were edited during the literature analysis stage.
- This markdown file is the saved context artifact requested afterward.

## High-Level Process Followed

1. Read and analyze the current project context.
2. Inspect the PDF-reading notebook at `C:\GIT\r_proposal\scripts\read_pdf.ipynb`.
3. Inventory the research corpus in `C:\GIT\r_proposal\research`.
4. Extract titles, page counts, and abstract-like snippets from the papers.
5. Read more closely the papers most relevant to a thesis on limit order books, market making, regime detection, execution probability, and market microstructure.
6. Synthesize the literature gap and align it with the thesis contributions already present in the pasted thesis draft.
7. Draft a detailed abstract, introduction, and updated `ref.bib` content in copiable format.

## Project Files Reviewed

### Main Project Files

- `C:\GIT\r_proposal\main.tex`
- `C:\GIT\r_proposal\ref.bib`
- `C:\GIT\r_proposal\scripts\read_pdf.ipynb`

### Observation About Thesis Source

The repository contains `main.tex` for a proposal-style document. The longer chapter-based thesis content with:

- `\chapter{Introduction}`
- `\chapter{Representation of the Limit Order Book}`
- `\chapter{Regime Selection}`
- `\chapter{Market Making Price Bands and Execution Modeling}`
- `\chapter{Implementation and Future Scope}`

was not found as a file in the workspace and was instead supplied in the conversation. The writing output below is therefore aligned to the pasted thesis draft, not only to `main.tex`.

## Notebook Analysis

File reviewed: `C:\GIT\r_proposal\scripts\read_pdf.ipynb`

### Notebook Purpose

The notebook is designed to read a PDF and extract research-review assets:

- full text
- page previews
- embedded images
- table-like data
- equation-like lines
- section-level summaries

### Notebook Dependencies

The notebook expects:

- `pymupdf` via `fitz`
- `pandas`
- `matplotlib`
- `pillow`
- optional `openai`

### Notebook Workflow Summary

The notebook performs the following major steps:

1. Set `PDF_PATH` and `OUTPUT_DIR`.
2. Extract each page into line-based text.
3. Detect equation-like lines using regex and character heuristics.
4. Render page previews to PNG.
5. Extract embedded images.
6. Extract tables when available.
7. Build a JSON manifest containing page text, metadata, images, tables, and full text.
8. Build extractive summaries for numbered sections.
9. Optionally call an OpenAI model for section summarization.

### Key Notebook Functions Observed

- `clean_text`
- `extract_page_lines`
- `is_equation_like`
- `render_page_preview`
- `extract_embedded_images`
- `extract_tables_from_page`
- `extract_pdf_bundle`
- `collect_assets_from_pages`
- `sentence_split`
- `extractive_summary`
- `extract_section_by_number`
- `section_summaries`
- `summarize_with_openai`

### Environment Note

When the workflow was first tested, `fitz` was missing from the environment. The package set required by the notebook was then installed so the extraction approach could follow the notebook logic rather than switching to a different parser.

## Research Corpus Inventory

The following PDFs were found in `C:\GIT\r_proposal\research` at review time:

- `Which Free Lunch Would You Like TodaySir DeltaHedgingVolatility.pdf`
- `kelly-yudovina (2017) a-markov-model-of-a-limit-order-book-thresholds-recurrence-and-trading-strategies.pdf`
- `Sahalia and Xiu (2019) AHausmantest for the presence of market microstructure.pdf`
- `Roman Gayduk and Sergey Nadtochiy (2018) Liquidity effects of trading frequency,.pdf`
- `RL for HEDGING .pdf`
- `Maxine et al. (2026) TradeFM- A Generative Foundation Model for tradeflow and Market Microstructure_JP Morgan.pdf`
- `Market_Agents.pdf`
- `ML methood for LOB.pdf`
- `Justin Sirignano and Rama Cont (2018) Unifversal features of price formation in FInancial Markets- perspectives from Deep Learning.pdf`
- `Jain et al. (2023) Limit_Order_Book_Simulation_Review.pdf`
- `FinanceProj.pdf`
- `Direct Estimation of Equity market impact.pdf`
- `DeepNet Jump D Bloch.pdf`
- `Deep learning regime portfolio.pdf`
- `Deep Learning Ensemble strategy.pdf`
- `Avellaneda-Stoikov-(2008)_high_frequency_trading_in_a_limit_order_book_2_version.pdf`
- `Avellaneda-Stoikov-(2008)_high_frequency_trading_in_a_limit_order_book.pdf`
- `Alexander Schied and Tao Zhang, (2019) A market impact game under transient price impact.pdf`
- `9_optimal_dealer_pricing.pdf`
- `8_a_theory_of_power-law_listributions_in_linancial_market_activity.pdf`
- `7_market_microstructure.pdf`
- `6_market_making_and_mean_reversion.pdf`
- `5_hyperquant_crypto.pdf`
- `4_Gueant-Lehalle_dealing_with_the_inventory_risk.pdf`
- `3_Bayraktar-Ludkovski_optimal_trade_execution_in_iliquid_markets.pdf`
- `12_Fernandez_Tapia_thesis.pdf`
- `11_authomated_market_making.pdf`
- `10_statistical_properties_of_stock_orderbooks.pdf`
- `Emil S. Jorgensen and Michael Sorensen (2026) Prediction-based inference for integrated diffusions with.pdf`

## Papers Prioritized for Thesis Writing

The following were treated as primary references for a thesis on LOB-based market making:

- Jain et al. (2023), LOB simulation review
- Kelly and Yudovina (2018), Markov model of a limit order book
- Bouchaud, Mezard, Potters, statistical properties of stock order books
- Avellaneda and Stoikov (2008), high-frequency trading in a limit order book
- Gueant, Lehalle, Fernandez-Tapia, inventory-risk market making
- Gayduk and Nadtochiy (2018), liquidity effects of trading frequency
- Schied and Zhang (2019), transient price impact game
- Ait-Sahalia and Xiu (2019), market microstructure noise test
- Sirignano and Cont (2018), universal features of price formation
- Bertia and Kasneci (2025), TLOB
- TradeFM (2026), generative foundation model for microstructure

The following were treated as secondary or supporting context:

- Direct estimation of equity market impact
- DeepNet jump models
- Market agents and tacit collusion
- RL for hedging
- Deep learning ensemble trading
- Deep learning regime portfolio
- Bayraktar and Ludkovski on execution in illiquid markets
- Fernandez-Tapia thesis
- Automated market making survey/model
- Broad market microstructure survey

## Core Takeaways from the Main Papers

### Jain et al. (2023) - Limit Order Book Simulations: A Review

- Good survey of the LOB modeling landscape.
- Emphasizes the difficulty of building realistic LOB simulators.
- Useful for positioning the thesis within parametric, statistical, agent-based, and ML approaches.
- Supports the claim that simulation, execution modeling, and backtesting are difficult and central.

### Kelly and Yudovina (2018) - Markov Model of a Limit Order Book

- Provides a tractable stochastic model of short-horizon LOB dynamics.
- Useful for theoretical grounding in recurrence, thresholds, and trading implications.
- Supports the thesis narrative that structural probabilistic models remain important.

### Bouchaud, Mezard, Potters - Statistical Properties of Stock Order Books

- Documents broad statistical regularities in order placement and book shape.
- Supports empirical motivation for feature design around depth, queue structure, and heavy tails.
- Helpful for justifying data-driven, stylized-fact-aware modeling.

### Avellaneda and Stoikov (2008)

- Canonical inventory-aware market-making model.
- Frames quote placement as a trade-off between spread capture and inventory risk.
- Important baseline for the market-making chapter, especially in contrasting parametric intensities with empirical fill estimation.

### Gueant, Lehalle, Fernandez-Tapia

- Extends inventory-based market making into a stronger control framework.
- Useful for linking quote dynamics, inventory constraints, and asymptotic quote structure.
- Supports the thesis claim that execution and inventory cannot be studied separately.

### Gayduk and Nadtochiy (2018) - Liquidity Effects of Trading Frequency

- Highlights that higher trading frequency may improve efficiency but also increase fragility.
- Relevant for motivating regime dependence and caution in liquidity provision.

### Schied and Zhang (2019) - Market Impact Game

- Shows strategic interaction under transient impact and competition.
- Useful as a reminder that execution conditions depend on strategic behavior, not only passive queue mechanics.

### Ait-Sahalia and Xiu (2019)

- Important econometric context for high-frequency data quality and microstructure noise.
- Useful for keeping claims about high-frequency inference disciplined.

### Sirignano and Cont (2018)

- Strong evidence for universal, path-dependent price formation mechanisms in high-frequency order-book data.
- Useful for motivating temporal dependence and richer data-driven state representations.

### TLOB (2025)

- Shows that modern sequence models can capture temporal and spatial dependencies in LOB data.
- Also points out that prediction quality does not directly imply tradable profitability after transaction costs.
- This is directly relevant to the thesis distinction between prediction and execution-aware market making.

### TradeFM (2026)

- Suggests cross-asset, scale-invariant microstructure representations and realistic synthetic rollouts.
- Useful for future-scope discussion around simulation, generalization, and learning-based agents.

## Main Literature Gap Identified

The central literature gap used for drafting was:

- many models identify market states but do not connect them directly to execution decisions
- many predictive ML papers target short-term price movement rather than quote placement
- classical market-making models often assume stylized execution intensities instead of empirically estimating regime-specific fill behavior
- standard clustering methods are static and ignore persistence and transitions in market state

This led to the thesis positioning:

- identify LOB regimes from microstructure features
- classify incoming states online
- estimate empirical bid/ask execution probabilities conditional on regime
- use those probability surfaces to choose market-making quote distances

## Interpretation of the User's Thesis Position

Based on the pasted thesis draft, the project was interpreted as having the following structure:

- represent the LOB using level-2 or depth-based snapshot features
- compute interpretable microstructure features such as spread, imbalance, microprice, queue imbalance, depth slope, and flow metrics
- identify latent regimes using baseline clustering and then more dynamic models such as HMMs
- estimate fill probabilities across distance and volume buckets
- turn those estimates into a market-making framework for quote selection
- leave room for online classification, recalibration, and later reinforcement learning

## Drafting Principles Used

The abstract and introduction were drafted to:

- stay close to the pasted thesis structure and claims
- strengthen academic framing and literature flow
- avoid overstating empirical results that were not yet demonstrated in the thesis text
- connect classical microstructure theory with modern data-driven modeling
- keep regime detection and execution modeling as the central thesis contribution

## Draft Abstract Produced in Session

```latex
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

Modern electronic financial markets are organized around the limit order book (LOB), where the continuous interaction of limit orders, market orders, and cancellations determines short-horizon price formation and liquidity dynamics. For market makers, the LOB is both an opportunity and a source of risk: tighter quotes may improve execution probability, but they also increase exposure to adverse selection, inventory imbalance, and rapid microstructural regime shifts. This thesis develops a data-driven and execution-aware framework for market making in LOB environments by linking market-state identification directly to quote placement.

The proposed framework begins by representing each LOB snapshot through a set of microstructure features, including spread, imbalance, depth, queue pressure, and liquidity-sensitive price measures such as mid-price and microprice. These features are used to identify latent market regimes that summarize the prevailing liquidity and order flow conditions. K-means clustering is employed as a transparent baseline segmentation method, while more expressive probabilistic and sequential alternatives such as Gaussian mixture models and hidden Markov models are considered to capture overlapping states and temporal persistence. This regime layer is then coupled with an online classification mechanism that assigns incoming market states to regimes in real time.

The central contribution of the thesis is the integration of regime detection with empirical execution modeling. For each regime, fill probabilities of passive bid and ask orders are estimated as functions of distance from the mid-price and order size over a fixed horizon. These regime-specific execution surfaces provide an operational bridge between descriptive LOB modeling and market-making decisions: they quantify the trade-off between spread capture and execution likelihood, and thereby support adaptive quote selection under changing market conditions. The framework also accommodates dynamic recalibration so that execution surfaces and regime assignments can be updated as new data arrive.

Conceptually, the thesis is positioned between classical stochastic-control models of market making and modern data-driven approaches to microstructure analysis. Rather than relying exclusively on restrictive parametric assumptions or purely predictive black-box models, it proposes a modular architecture in which interpretable state variables, latent regime structure, and empirically estimated fill dynamics interact within a scalable decision pipeline. The resulting framework is intended not only as a basis for practical market-making logic, but also as a research platform for future work on sequential regime learning, reinforcement learning, simulator design, and control-theoretic inventory management in high-frequency markets.
```

## Draft Introduction Produced in Session

```latex
\chapter{Introduction}
\thispagestyle{plain}

Modern financial markets are predominantly organized around the limit order book (LOB), a continuously evolving record of outstanding buy and sell orders submitted at different prices and quantities. In electronic double-auction markets, every limit order, market order, and cancellation updates the local balance between supply and demand, making the LOB the fundamental object through which liquidity, queue priority, and short-horizon price formation are expressed. For this reason, the analysis of LOB dynamics lies at the heart of market microstructure research and is central to high-frequency applications such as optimal execution, market making, and intraday risk management.

The growing availability of high-frequency market data has made it possible to study the LOB at a much finer level of granularity than was previously feasible. Empirical work has documented persistent structural regularities in order submission and book shape, including heavy-tailed order placement, nontrivial depth profiles, and recurrent statistical patterns across assets and markets \cite{statOB}. At the same time, the econometric use of ultra-high-frequency data is complicated by market microstructure noise, discreteness, and sampling effects, which imply that model design must remain sensitive not only to economic structure but also to measurement frictions \cite{HausmanTest}. These observations motivate a framework that is both empirically grounded and robust to the noisy, non-stationary nature of modern order-driven markets.

A large strand of the literature approaches the LOB through parsimonious stochastic or control-theoretic models. Structural models of dealer behavior, beginning with classical inventory-based pricing formulations, characterize the trade-off between spread capture and inventory risk \cite{OptimalDealerPricing}. In the context of electronic order books, Avellaneda and Stoikov formulate market making as a utility-maximization problem in which quote placement depends on reservation prices, inventory, and execution intensities \cite{ASModel}. Extensions by Gueant, Lehalle, and Fernandez-Tapia develop a more detailed stochastic-control treatment of inventory-constrained quoting and provide tractable asymptotic approximations for optimal bid and ask quotes \cite{GueantLehalleFernandezTapia}. Complementing these execution-focused models, Kelly and Yudovina develop a Markovian LOB framework that yields threshold behavior, recurrence properties, and insights into high-frequency trading strategies \cite{MarkovLOB}. Related work on trading frequency, market impact, and control-stopping games further shows that liquidity provision cannot be studied in isolation from strategic interaction, execution timing, and dynamic market fragility \cite{LiqFreq,impactGame,StopGame}.

A second strand of the literature uses machine learning and large-scale data-driven methods to model microstructure dynamics. Deep learning studies provide evidence that order-book states contain strong nonlinear and path-dependent information about short-term price variation \cite{UnivFeatures}. More recent architectures such as TLOB use temporal and spatial attention mechanisms to capture dependencies within LOB data and improve prediction across multiple horizons \cite{TLOB}. At a broader scale, TradeFM extends this direction by learning transferable representations from large event streams across many assets, suggesting that certain aspects of market microstructure may admit cross-asset generalization and synthetic-data generation \cite{TradeFM}. These methods substantially improve representation learning and prediction, but their main focus is typically on price-direction forecasting, sequence modeling, or simulation fidelity rather than on the direct construction of execution-aware quoting policies.

This distinction is important for market making. In practice, a market maker must decide not only whether prices are likely to move, but also where to post passive orders, how execution likelihood changes with quote distance and size, and when prevailing conditions are favorable enough to provide liquidity. A comprehensive review of LOB simulation and modeling approaches shows that the literature spans zero-intelligence models, queueing formulations, Hawkes-type processes, agent-based simulators, and learning-based models, each with different trade-offs in realism, tractability, and usefulness for downstream trading tasks \cite{LOBRev}. Yet a persistent gap remains between \emph{regime identification} and \emph{execution strategy design}. Many studies segment market states, predict future prices, or simulate order flow, but comparatively fewer frameworks directly connect latent market conditions to regime-specific execution probabilities and quote-selection rules.

This thesis addresses that gap by proposing a unified, data-driven framework for market making in LOB environments. The core idea is to treat market making as a sequential decision problem conditioned on latent microstructural regimes. First, features derived from the LOB are used to identify distinct market states associated with different combinations of spread, liquidity, imbalance, and order-flow pressure. Second, incoming observations are classified online into these regimes. Third, for each regime, empirical fill probabilities are estimated for bid and ask orders as functions of distance from the mid-price and order size. These regime-conditioned execution surfaces are then used to construct adaptive quoting rules that explicitly balance the trade-off between execution likelihood and spread capture.

The framework is intentionally positioned between classical parametric modeling and purely black-box prediction. On one hand, it preserves interpretability by working with economically meaningful LOB features and by separating state identification from execution estimation. On the other hand, it remains flexible enough to incorporate probabilistic clustering, hidden-state dynamics, and future learning-based decision layers. This makes the framework suitable not only for the immediate market-making application studied in this thesis, but also as a foundation for later work on simulator-based evaluation, reinforcement learning, and control-theoretic inventory management.

\section{Literature Gap}

Existing approaches to LOB modeling can be broadly grouped into structural stochastic models, econometric or statistical learning methods, and modern deep learning approaches. Structural models offer interpretability and clear economic mechanisms, but they often rely on simplifying assumptions regarding arrival intensities, stationarity, or the form of execution dynamics. Data-driven methods are more flexible, but many of them are designed for prediction accuracy rather than decision support. In particular, a large part of the recent literature is centered on forecasting short-term price movements, learning general representations of order flow, or generating synthetic microstructure data \cite{UnivFeatures,TLOB,TradeFM}. These advances are important, but they do not directly solve the quoting problem faced by a market maker.

A major limitation across the literature is the weak integration between \emph{state inference} and \emph{execution modeling}. Even when market states or regimes are identified, they are often treated as descriptive outputs rather than as inputs to an execution-aware policy. Conversely, classical market-making models typically encode execution through stylized intensity functions instead of estimating fill behavior empirically from data. This leaves open a practical question: how should a market maker translate a detected regime into concrete bid and ask distances that are consistent with observed fill probabilities and adverse-selection risk?

A second limitation is that many segmentation methods are static. Standard clustering procedures such as K-means assign each snapshot independently, ignoring persistence and transitions in market conditions. However, LOB states are inherently sequential: liquidity stress, directional pressure, and balanced quoting environments tend to persist over short horizons rather than appearing as isolated observations. Ignoring this temporal dependence can lead to unstable state assignments and, in turn, unstable quote-selection logic.

A third limitation concerns the operational interface between model outputs and trading actions. For market making, the relevant output is not only a regime label or a predicted price move, but a regime-conditioned estimate of execution likelihood across candidate quote levels. Without this layer, it is difficult to compare the expected benefit of quoting near the touch against the larger spread available deeper in the book. This thesis is motivated by the need for a framework that joins these elements in a computationally tractable way.

\section{Contributions}

In response to the above gaps, this thesis makes the following contributions:

\begin{enumerate}
    \item \textbf{Feature-based market-state representation:} We construct a compact but expressive representation of the LOB using microstructure features such as spread, imbalance, depth, queue pressure, and liquidity-sensitive price measures. This representation is designed to retain economic interpretability while remaining suitable for real-time computation.

    \item \textbf{Regime identification framework:} We propose a regime-detection layer for LOB states, using K-means as an interpretable baseline and allowing extensions to probabilistic and sequential latent-state models such as Gaussian mixture models and hidden Markov models. This provides a practical way to partition the market into distinct liquidity and order-flow environments.

    \item \textbf{Online regime classification:} We develop an online mechanism that maps incoming LOB observations to the learned regimes in real time. This enables the market-making policy to adapt continuously as market conditions evolve.

    \item \textbf{Regime-conditioned execution probability modeling:} For each regime, we estimate empirical fill probabilities for passive bid and ask orders as functions of distance from the mid-price and order size over a fixed horizon. This yields execution-probability surfaces that directly quantify the trade-off between execution likelihood and spread capture.

    \item \textbf{Execution-aware market-making logic:} By combining latent regime information with empirical fill surfaces, we construct a market-making framework that selects quote levels conditionally on the prevailing microstructural state. The objective is to improve the alignment between liquidity provision, inventory discipline, and observed execution behavior.

    \item \textbf{Scalable and extensible pipeline:} The overall architecture is designed to be modular and computationally tractable, making it suitable for high-frequency environments and extensible to future work on reinforcement learning, synthetic-data generation, and control-based trade management.
\end{enumerate}

\section{Paper Organization}

The remainder of the paper is organized as follows. Chapter 2 describes the representation of the limit order book and the construction of microstructure features used to characterize market state. Chapter 3 develops the regime-identification methodology and compares alternative approaches for partitioning LOB dynamics into economically meaningful states. Chapter 4 introduces the execution-probability framework and shows how regime-conditioned fill surfaces can be used to construct adaptive market-making quote bands. Chapter 5 discusses implementation aspects, including a data-driven continuous-time Markov chain perspective and directions for future research.
```

## Bibliography Entries Prepared in Session

```bibtex
@article{LOBRev,
  title={Limit Order Book Simulations: A Review},
  author={Jain, Konark and Firoozye, Nick and Kochems, Jonathan and Treleaven, Philip},
  journal={SSRN Electronic Journal},
  note={SSRN 4745587},
  year={2023}
}

@article{MarkovLOB,
  title={A Markov Model of a Limit Order Book: Thresholds, Recurrence, and Trading Strategies},
  author={Kelly, Frank and Yudovina, Elena},
  journal={Mathematics of Operations Research},
  volume={43},
  number={1},
  pages={181--203},
  year={2018}
}

@article{TLOB,
  title={{TLOB}: A Novel Transformer Model with Dual Attention for Price Trend Prediction with Limit Order Book Data},
  author={Bertia, Leonardo and Kasneci, Gjergji},
  journal={arXiv preprint arXiv:2502.15757},
  year={2025}
}

@article{StopGame,
  title={Control-stopping Games for Market Microstructure and Beyond},
  author={Gayduk, Roman and Nadtochiy, Sergey},
  journal={Mathematics of Operations Research},
  volume={45},
  year={2020}
}

@article{statOB,
  title={Statistical Properties of Stock Order Books: Empirical Results and Models},
  author={Bouchaud, Jean-Philippe and Mezard, Marc and Potters, Marc},
  journal={arXiv preprint cond-mat/0203511},
  year={2002}
}

@article{OptimalDealerPricing,
  title={Optimal Dealer Pricing Under Transactions and Return Uncertainty},
  author={Ho, Thomas and Stoll, Hans R.},
  journal={Journal of Financial Economics},
  volume={9},
  number={1},
  pages={47--73},
  year={1981}
}

@article{ASModel,
  title={High-frequency Trading in a Limit Order Book},
  author={Avellaneda, Marco and Stoikov, Sasha},
  journal={Quantitative Finance},
  volume={8},
  number={3},
  pages={217--224},
  year={2008}
}

@article{GueantLehalleFernandezTapia,
  title={Dealing with the Inventory Risk: A Solution to the Market Making Problem},
  author={Gueant, Olivier and Lehalle, Charles-Albert and Fernandez-Tapia, Joaquin},
  journal={Mathematics and Financial Economics},
  volume={7},
  number={4},
  pages={477--507},
  year={2013}
}

@article{LiqFreq,
  title={Liquidity Effects of Trading Frequency},
  author={Gayduk, Roman and Nadtochiy, Sergey},
  journal={Mathematical Finance},
  volume={28},
  number={3},
  pages={839--876},
  year={2018}
}

@article{impactGame,
  title={A Market Impact Game under Transient Price Impact},
  author={Schied, Alexander and Zhang, Tao},
  journal={Mathematics of Operations Research},
  volume={44},
  number={1},
  pages={102--121},
  year={2019}
}

@article{HausmanTest,
  title={A Hausman Test for the Presence of Market Microstructure Noise in High Frequency Data},
  author={Ait-Sahalia, Yacine and Xiu, Dacheng},
  journal={Journal of Econometrics},
  volume={211},
  number={1},
  pages={176--205},
  year={2019}
}

@article{UnivFeatures,
  title={Universal Features of Price Formation in Financial Markets: Perspectives from Deep Learning},
  author={Sirignano, Justin and Cont, Rama},
  journal={arXiv preprint arXiv:1803.06917},
  year={2018}
}

@article{TradeFM,
  title={{TradeFM}: A Generative Foundation Model for Trade-flow and Market Microstructure},
  author={Kawawa-Beaudan, Maxime and Sood, Srijan and Papasotiriou, Kassiani and Borrajo, Daniel and Veloso, Manuela},
  journal={arXiv preprint arXiv:2602.23784},
  year={2026}
}
```

## Notes on Scope and Limitations

- Not every paper in the folder was equally relevant to the exact thesis topic.
- The strongest inputs for the abstract and introduction came from the LOB, market-making, execution, and microstructure-regime papers listed above.
- The review performed here was designed to support thesis writing and positioning, not to produce a full annotated bibliography for every PDF in the folder.
- Because the thesis draft was provided in chat rather than as a file, any later wording changes in the thesis file should be checked against the draft text saved here.

## Recommended Next Use of This File

Use this file as the recovery context for future work on:

- revising the thesis introduction
- rewriting the abstract
- expanding the literature review chapter
- updating `ref.bib`
- aligning chapter claims with citations
- converting the regime section into a more formal methodology chapter

## Session Outcome Summary

This review session produced:

- a structured reading of the available research corpus
- a synthesis of the main literature gap
- a thesis-aligned abstract draft
- a thesis-aligned introduction draft
- a cleaned set of core bibliography entries for the cited works
