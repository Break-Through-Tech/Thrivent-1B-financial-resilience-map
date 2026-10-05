# Introduction to the [Codebook](https://www.federalreserve.gov/consumerscommunities/files/SHED_2025codebook.pdf):

The codebook explains exactly what each variable in the 2025 Survey of Household Economics and Decisionmaking (SHED) dataset means, how it is coded, the kinds of people asked each question, and what values appear in the data.

The survey is designed to measure the economic circumstances of U.S. adults. It covers much more than income. The variables in this codebook include topics such as:
- financial well-being
- employment
- childcare and caregiving
- housing and rent
- homeowners insurance
- natural disasters
- banking
- fraud and scams
- credit access
- credit cards
- Buy Now, Pay Later
- cryptocurrency
- education
- student loans
- retirement
- investments
- income and government benefits
- inflation
- emergency savings
- bill payment difficulties
- food sufficiency
- health-care affordability
- demographic characteristics

## Types of Questions asked / Answers received (to keep in mind while interpreting / cleaning data):
- Binary: 0 No, 1 Yes
- Select all that apply: answers became multiple separate binary variables, each answer coded separately (0 No, 1 Yes). DO NOT treat as mutually exclusive categories
- Skip Logic: some questions depend on answers to earlier questions (ex a respondent doesn’t have student loans so student loan questions don’t apply and that respondent isn’t asked certain questions)
- Special negative codes: make sure to check what the codes mean for each question since they can correspond to different answers depending on the context
- Survey design variation: for some questions, surveyors randomly divide respondents into groups and show different versions of the question to study how respondents react to different hypothetical conditions
- Missing does not necessarily mean "unknown." Sometimes refusal and "don't know" are coded explicitly rather than treated as standard missing data. It can mean:
  - respondent was not eligible for the question
  - respondent was intentionally skipped because of survey logic
  - question appeared only to a randomized subsample
  - respondent refused
  - respondent did not know
  - actual data were unavailable

## Prefixes for navigating data (rough order)

| Variable family | Main topic |
| --------- | --------------- |
| L... | Household composition |
| B... | Financial well-being |
| X... | Financial concerns |
| CG... | Childcare/caregiving |
| D... | Employment/work |
| GH... | Housing/homeowners insurance |
| R... | Renting/moving |
| M... | Mortgage |
| ND... | Natural disasters/severe weather |
| BK... | Banking/fraud |
| A... | Credit applications/access |
| C... | Credit cards |
| BNPL... | Buy Now, Pay Later |
| S... | Cryptocurrency |
| ED... | Education |
| SL... | Student loans |
| K... | Retirement/assets |
| DC... | Investment comfort |
| FL... | Risk tolerance |
| I... | Income |
| FS... | Financial support
| INF... | Inflation |
| EF... | Emergency finances |
| FD... | Food sufficiency |
| E... | Medical and unexpected expenses |
| pp... | Demographic/profile variables

## Glossary of terms:
- SHED: Survey of Household Economics and Decisionmaking
- Weight variables:
  - weight: main sample weight, normally used for the percentages, averages, regressions, and descriptive statistics
  - weight_pop: population weight, weights sum approximately to the size of the relevant U.S. population instead of sample size used in survey
  - panel_weight & panel_weight_pop: apply to people who participated in both the 2024 and 2025 surveys, allows longitudinal or panel-style analysis
- Cross-sectional analysis: Looks at respondents at one point in time (2025 survey)
- Panel analysis: Tracks the same individuals over multiple survey waves (use panel weights)
  - pp prefix: demographic profile variables collected by Ipsos
  - ppage: Exact age
  - ppagecat: Age grouped into seven categories (18–24, 25–34, 35–44, 45–54, 55–64, 65–74, 75+)
  - ppeduc5: Education grouped into five categories
  - ppemploy: Current employment status
  - pphhsize: Household size
  - ppinc7: Household income categories
- Refused: Respondent declined to answer a question. Often given its own code such as -1.
- Don't know: Respondent could not provide an answer. Frequently represented with a special code such as -2.
- Not asked: Respondent was not presented with the question.
- Survey weight: Number indicating how much a respondent contributes toward estimates of the target population.
- Post-stratification weight: Weight adjusted so that sample characteristics better align with known population characteristics.
- Cross-sectional data: Data representing people at one point or period in time.
- Longitudinal data: Data following the same individuals across time
- BNPL: Buy Now, Pay Later, a financing arrangement that divides purchases into payments.
- NSF fee: Non-sufficient-funds fee, charged when an account lacks enough money to cover a transaction.
- Overdraft: Transaction that causes an account balance to fall below available funds, potentially resulting in fees.
- P2P payment: Person-to-person electronic payment, such as Venmo, Zelle, Cash App, or similar services.
- Defined-benefit pension: Retirement plan promising a defined payment, often monthly, after retirement.
- 401(k): Employer-sponsored defined-contribution retirement account.
- IRA: Individual Retirement Account.
- Roth IRA: Retirement account generally funded with after-tax contributions and subject to Roth tax rules.
- Asset: Something of economic value owned by a person or household.
- Investable assets: Financial resources potentially available for investment, such as savings and securities.
- EITC: Earned Income Tax Credit.
- SNAP: Supplemental Nutrition Assistance Program, commonly called food stamps.
- WIC: Special Supplemental Nutrition Program for Women, Infants, and Children.
- SSI: Supplemental Security Income.
- TANF: Temporary Assistance for Needy Families.
- MSA: Metropolitan Statistical Area.
